# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """Manage courses, session in academy""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ros Krotov",
    'website': "http://route.in.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test module',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}