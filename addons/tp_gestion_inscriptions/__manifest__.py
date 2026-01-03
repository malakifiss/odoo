{
    'name': 'Gestion des Inscriptions',
    'version': '1.0',
    'summary': 'Gestion des inscriptions simples',
    'description': 'Module Odoo pour gérer des inscriptions simples',
    'author': 'Your Name',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/inscription_views.xml',
    ],
    'installable': True,
    'application': True,
}
