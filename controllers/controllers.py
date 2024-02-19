# -*- coding: utf-8 -*-
# from odoo import http


# class Laligamodulo(http.Controller):
#     @http.route('/laligamodulo/laligamodulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/laligamodulo/laligamodulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('laligamodulo.listing', {
#             'root': '/laligamodulo/laligamodulo',
#             'objects': http.request.env['laligamodulo.laligamodulo'].search([]),
#         })

#     @http.route('/laligamodulo/laligamodulo/objects/<model("laligamodulo.laligamodulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('laligamodulo.object', {
#             'object': obj
#         })
