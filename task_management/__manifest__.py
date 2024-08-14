{
    'name': 'Task Management',
    'version': '1.0',
    'summary': 'Manage a list of tasks',
    'author': 'Ingeniero Jhonatan Rocha',
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/task_views.xml',
    ],
    'installable': True,
    'application': True,
}
