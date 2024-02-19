# -*- coding: utf-8 -*-
{
    'name': "laligamodulo",
    'summary': """
        Gestión de LaLiga: jugadores, partidos, entrenadores, equipos y estadios""",
    'description': """
        Gestiona LaLiga con clases para jugadores, partidos, entrenadores, equipos y estadios, cada uno con sus propios campos y relaciones
    """,
    'author': "Miguel Ángel Torregrosa Calvo",
    'website': "https://www.buscatupeli.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'web'], #web sustituye al módulo report que ha quedado anticuado
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_player.xml',
        'reports/report_coach.xml',
        'reports/report_match.xml',
        'reports/report_stadium.xml',
        'reports/report_team.xml',
        'data/data.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}