# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2012 OpenERP s.a. (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'OpenID Connect Authentication',
    'version': '1.0',
    'category': 'Tools',
    'description': """
Allow users to login through OpenID Connect Provider.
=====================================================
""",
    'author': 'Graeme Gellatly',
    'maintainer': 'Graeme Gellatly',
    'website': 'http://www.openerp.com',
    'external_dependencies': {'python': [
        'pyJWT',
        'cryptography'
    ]},
    'depends': ['auth_oauth'],
    'data': [
        'views/auth_oidc_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
