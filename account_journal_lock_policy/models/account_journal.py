# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import date, timedelta, datetime
from dateutil.rrule import rrule, DAILY
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT


class AccountJournal(models.Model):

    _inherit = 'account.journal'

    enforce_lock = fields.Boolean(default=False)
    days = fields.Integer()
    day_type = fields.Selection([
        ('weekday', 'working days'),
        ('day', 'days')])
    months = fields.Integer()
    cutoff_type = fields.Selection(
        [('date', 'transaction date'),
         ('eom', 'end of month following transaction')])

    @api.multi
    def _check_lock_date(self, move):
        if not self.enforce_lock:
            return False
        today = datetime.strptime(fields.Date.context_today(move),
                                  DEFAULT_SERVER_DATE_FORMAT)
        transaction_date = datetime.strptime(move.date, DEFAULT_SERVER_DATE_FORMAT)
        if self.cutoff_type == 'eom':
            transaction_date += relativedelta(day=31)
        if self.months:
            transaction_date += relativedelta(months=self.months)
        if self.days:
            weekdays = range(5 if self.day_type == 'weekday' else 7)
            transaction_date = rrule(
                DAILY, interval=self.days, byweekday=weekdays,
                dtstart=transaction_date)
            transaction_date = transaction_date[1]
        if transaction_date > today:
            return True
        return False


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.multi
    def _check_lock_date(self):
        res = super(AccountMove, self)._check_lock_date()
        for move in self:
            lock_date = move.journal_id._check_lock_date(move)
            if lock_date:
                raise UserError(_("The transaction date is too old for the "
                                  "%s lock policy.") % move.journal_id.name)
        return res
