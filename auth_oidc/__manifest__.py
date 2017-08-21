# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'OpenID Connect Authentication',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Graeme Gellatly',
    'website': 'https://o4sb.com',
    'description': """
Allow users to login through OpenID Connect Provider.
=====================================================

Currently only tested on Azure AD and implicit flow needs
to be enabled.

""",
    'external_dependencies': {'python': [
        'pyjwt',
        'cryptography'
    ]},
    'depends': ['auth_oauth'],
    'data': [
        'views/auth_oidc_view.xml',
    ],
}
