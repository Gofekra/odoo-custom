# -*- coding: utf-8 -*-
{
    'name': "Facturación Electronica MyR",

    'summary': """
        Facturación Electrónica 2018""",

    'description': """
        Facturación Electrónica 2018
    """,

    'author': "MYR CONSULTORIA EN SISTEMAS SAC ",
    'website': "http://www.myrconsulting.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Facturacion_Electronica',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','account','odoope_einvoice_base','odoope_ruc_validation','odoope_toponyms'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        #'security/access_rules.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}