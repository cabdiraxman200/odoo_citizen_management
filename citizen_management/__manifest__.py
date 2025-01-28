{
    'name': 'Citizen Management System',
    'version': '1.0',
    'summary': 'Manage citizens and locations effectively',
    'author': 'Abdirahman',
    'category': 'Administration',
    "sequence": -100,
    'depends': ['mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/state_views.xml',
        'views/region_views.xml',
        'views/district_views.xml',
        'views/citizen_views.xml',
        'views/birth_views.xml',
        'views/death_views.xml',
        'views/marriage_views.xml',
        'views/divorce_views.xml',




    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
