# -*- coding: utf-8 -*-
{
    'name': "SparkIt Facilitator Weekly Reports",

    'summary': """
        Facilitator weekly reports addon module for management.""",

    'description': """
        Creates a form and a topbar menu item. Facilitators fill in their
        form on a weekly basis.
    """,

    'author': "Spark MicroGrants",
    'website': "http://www.sparkmicrogrants.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sparkit'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/facilitator_weekly_reports_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
