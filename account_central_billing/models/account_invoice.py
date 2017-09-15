# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountInvoice(models.Model):
    """inherits account.account_invoice and adds the order_partner_id field
    as well as overriding ORM functions to ensure the parent partner and order partner
    are written and created correctly"""
    _inherit = 'account.invoice'

    order_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Commercial Partner'
    )

    order_invoice_id = fields.Many2one(
        comodel_name='res.partner',
        string='Invoice Partner'
    )

    @api.multi
    def _get_invoice_partner(self):
        """
        Hook method for extensibility to determine which partner should be used
        for checking the lock date
        :return: A res.partner recordset
        """
        return super(AccountInvoice, self
                     )._get_invoice_partner() + self.order_partner_id

    @api.constrains('partner_id', 'order_partner_id')
    def check_company(self):
        for record in self:
            if record.company_id.partner_id.id in [
                    record.partner_id.id,
                    record.partner_id.commercial_partner_id.id]:
                raise ValidationError('Cannot self bill')

    @api.model
    def create(self, vals):
        """Function overrides create to ensure that parent account is
        always used"""
        if vals.get('partner_id'):
            Partner = self.env['res.partner']
            order_partner = Partner.browse(vals['partner_id'])
            partner = order_partner.commercial_partner_id
            inv_p_id = partner.get_billing_partner(vals)
            if inv_p_id != partner.id:
                vals.update({'partner_id': inv_p_id,
                             'order_partner_id': partner.id,
                             'order_invoice_id': order_partner.id})
        return super(AccountInvoice, self).create(vals)

    @api.multi
    def write(self, vals):
        """Function overrides create to ensure that parent account is
        always used"""
        if vals.get('partner_id', False):
            Partner = self.env['res.partner']
            partner = Partner.browse(vals['partner_id']).commercial_partner_id
            inv_p_id = partner.get_billing_partner(vals, self[0])
            if inv_p_id != partner.id:
                vals.update({'partner_id': inv_p_id,
                             'order_partner_id': partner.id,
                             'order_invoice_id': vals['partner_id']})
        return super(AccountInvoice, self).write(vals)

    @api.model
    def search(self, args, **kwargs):
        """override search so we find subsidiary invoices when looking at
        that partner.
        @note: this could break quite easily if used with multiple
        custom filters"""
        search_args = args[:]
        for arg in search_args:
            if arg[0] == 'partner_id' and arg[1] in [
                    '=', 'like', 'ilike', 'child_of']:
                args.remove(arg)
                args.extend(['|', arg, ('order_partner_id', arg[1], arg[2])])
                break
        return super(AccountInvoice, self).search(args, **kwargs)

    def _get_refund_common_fields(self):
        return super(AccountInvoice, self)._get_refund_common_fields() + [
            'order_partner_id', 'order_invoice_id']
