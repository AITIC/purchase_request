# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase Request',
    'version': '12.0',
    'category': 'Purchases',
    'author': "Boraq-Group",
    'summary': 'Purchase Request is an alternative simple module for Approvals in Odoo',
    'description': "Long description of module's purpose",
    'website': 'https://boraq-group.com',
    'depends': ['account','purchase','partner_autocomplete'],
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
