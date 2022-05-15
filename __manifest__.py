# -*- coding: utf-8 -*-
{
    'name': "geekmeet",

    'summary': """
        Manage a movie database for a geek shop club""",

    'description': """
        Manage a movie database for a geek shop club
    """,

    'author': "Alex Milan",
    'website': "https://ioc.xtec.cat/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Generic Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
