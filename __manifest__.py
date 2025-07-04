{
    'name': 'Real Estate Management',
    'version': '1.0.0',
    'description': """
        The Real Estate Advertisement module
    """,
    'summary': 'Manage real estate advertisements, listings, and inquiries',
    'author': 'ATS - Duong Hoang',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'auto_install': False,
    'application': True,
}
