# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase Request',
    'version': '13.0',
    'category': 'Purchases',
    'summary': 'Purchase Request is an alternative app for Approvals module',
    'description': "Long description of module's purpose",
    'website': 'https://boraq-group.com',
    'depends': ['account','purchase'],
    'data': [
        'views/requster.xml',
        'reports/report.xml',
        'reports/report_card.xml',
        'security/ir.model.access.csv', 
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
