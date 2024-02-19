# -*- coding: utf-8 -*-


from odoo import models, fields, api



class laligamodulo_player(models.Model):
    _name = 'laligamodulo.player'
    _description = 'Jugador de LaLiga'
    
    name = fields.Char(string='Nombre del Jugador', required=True, help="Introduce el nombre del jugador")
    position = fields.Selection([
        ('goalkeeper', 'Portero'),
        ('defender', 'Defensa'),
        ('midfielder', 'Mediocentro'),
        ('forward', 'Delantero')
    ], string='Posición')
    team_id = fields.Many2one('laligamodulo.team', string='Equipo', ondelete='set null')
    matches = fields.Many2many('laligamodulo.match', string='Partidos')
    goals = fields.Integer(string='Goles')
    assists = fields.Integer(string='Asistencias')
    yellow_cards = fields.Integer(string='Tarjetas Amarillas')
    red_cards = fields.Integer(string='Tarjetas Rojas')
    nationality = fields.Selection([
        ('es', 'España'),
        ('de', 'Alemania'),
        ('it', 'Italia'),
        ('fr', 'Francia'),
        ('uk', 'Reino Unido'),
        ('pt', 'Portugal'),
        ('nl', 'Países Bajos'),
        ('be', 'Bélgica'),
        ('se', 'Suecia'),
        ('br', 'Brasil'),
        ('ar', 'Argentina'),
        ('ot', 'Otro')
    ], string='Nacionalidad')
    age = fields.Integer(string='Edad')
    height = fields.Float(string='Altura')
    preferred_foot = fields.Selection([
        ('left', 'Izquierdo'),
        ('right', 'Derecho'),
        ('both', 'Ambos'),
        ('unknown', 'Desconocido'),
    ], string='Pie Preferido', default='unknown')
    goal_contributions = fields.Integer(string='Contribuciones de Goles', compute='_compute_goal_contributions', store=True)

    @api.depends('goals', 'assists')
    def _compute_goal_contributions(self):
        for i in self:
            i.goal_contributions = i.goals + i.assists



class laligamodulo_match(models.Model):
    _name = 'laligamodulo.match'
    _description = 'Partidos de LaLiga y los jugadores que jugaron'
    
    name = fields.Char(string='Partido', required=True, help="Introduce los dos equipos que se enfrentan")
    date = fields.Date(string='Fecha del Partido')
    high_risk_match = fields.Boolean(string='Partido de Alto Riesgo')
    stadium_id = fields.Many2one('laligamodulo.stadium', string='Estadio')
    player_ids = fields.Many2many('laligamodulo.player', string='Jugadores')
    
    
    
class laligamodulo_coach(models.Model):
    _name = 'laligamodulo.coach'
    _description = 'Entrenadores de equipos de LaLiga'
    
    name = fields.Char(string='Nombre del Entrenador', required=True, help="Introduce el nombre del entrenador")
    team_id = fields.Many2one('laligamodulo.team', string='Equipo', ondelete='set null')
    #un equipo puede tener varios entrenadores (el entrenador principal, el de porteros, etc)


class laligamodulo_team(models.Model):
    _name = 'laligamodulo.team'
    _description = 'Equipos de LaLiga'
    
    name = fields.Char(string='Equipo', required=True, help="Introduce el nombre del equipo")
    coach_id = fields.One2many('laligamodulo.coach', 'team_id', string='Entrenador')
    player_ids = fields.One2many('laligamodulo.player', 'team_id', string='Jugadores')
    wins = fields.Integer(string='Victorias', default=0)
    draws = fields.Integer(string='Empates', default=0)
    losses = fields.Integer(string='Derrotas', default=0)
    total_points = fields.Integer(string='Puntos Totales', compute='_compute_total_points', store=True)
    
    @api.depends('wins', 'draws', 'losses')
    def _compute_total_points(self):
        for i in self:
            i.total_points = i.wins * 3 + i.draws
            
  
  
class laligamodulo_stadium(models.Model):
    _name = 'laligamodulo.stadium'
    _description = 'Estadios de LaLiga'
    
    name = fields.Char(string='Estadio', required=True, help="Introduce el nombre del estadio")
    location = fields.Selection([
    ('alava', 'Álava'),
    ('albacete', 'Albacete'),
    ('alicante', 'Alicante'),
    ('almeria', 'Almería'),
    ('avila', 'Ávila'),
    ('badajoz', 'Badajoz'),
    ('barcelona', 'Barcelona'),
    ('burgos', 'Burgos'),
    ('caceres', 'Cáceres'),
    ('cadiz', 'Cádiz'),
    ('cantabria', 'Cantabria'),
    ('castellon', 'Castellón'),
    ('ciudad_real', 'Ciudad Real'),
    ('cordoba', 'Córdoba'),
    ('coruna', 'A Coruña'),
    ('cuenca', 'Cuenca'),
    ('girona', 'Girona'),
    ('granada', 'Granada'),
    ('guadalajara', 'Guadalajara'),
    ('guipuzcoa', 'Guipúzcoa'),
    ('huelva', 'Huelva'),
    ('huesca', 'Huesca'),
    ('illes_balears', 'Illes Balears'),
    ('jaen', 'Jaén'),
    ('leon', 'León'),
    ('lleida', 'Lleida'),
    ('lugo', 'Lugo'),
    ('madrid', 'Madrid'),
    ('malaga', 'Málaga'),
    ('murcia', 'Murcia'),
    ('navarra', 'Navarra'),
    ('ourense', 'Ourense'),
    ('palencia', 'Palencia'),
    ('pontevedra', 'Pontevedra'),
    ('rioja', 'La Rioja'),
    ('salamanca', 'Salamanca'),
    ('segovia', 'Segovia'),
    ('sevilla', 'Sevilla'),
    ('soria', 'Soria'),
    ('tarragona', 'Tarragona'),
    ('tenerife', 'Santa Cruz de Tenerife'),
    ('teruel', 'Teruel'),
    ('toledo', 'Toledo'),
    ('valencia', 'Valencia'),
    ('valladolid', 'Valladolid'),
    ('vizcaya', 'Vizcaya'),
    ('zamora', 'Zamora'),
    ('zaragoza', 'Zaragoza'),
    ('unknown', 'Desconocido')
], string='Ubicación', default='unknown')
    matches = fields.One2many('laligamodulo.match', 'stadium_id', string='Partidos')