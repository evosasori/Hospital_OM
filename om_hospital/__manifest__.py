# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
    Aplikasi SIMRS""",

    'description': """
        Aplikasi Untuk mengelola management rumah sakit 
    """,

    'author': "Cendana2000",
    'website': "https://www.cendana2000.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/pasien_tag_data.xml',
        'data/pasien.tag.csv',
        'views/templates.xml',
        'views/menu.xml',
        'views/pasien_perempuan.xml',
        'views/pasien_laki.xml',
        'views/appointment.xml',
        'views/patient.xml',
        'views/pasien_tag.xml',
        'wizard/batal_temu.xml',
        'views/sequence.xml',
        'views/odoo_playground.xml',
        'views/config_setting.xml',
        'views/operation.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    
}
