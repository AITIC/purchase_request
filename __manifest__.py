# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase Request1',
    'version': '1.2',
    'category': 'Purchases',
    'sequence': 60,
    'summary': 'Purchase orders, tenders and agreements',
    'description': "",
    'website': 'https://www.odoo.com/page/purchase',
    'depends': ['account','purchase'],
    'data': [
        'views/requster.xml',
        'reports/report.xml',
        'reports/report_card.xml',
        'security/ir.model.access.csv', 
    ],
    # 'demo': [
    #     'data/purchase_demo.xml',
    # ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
