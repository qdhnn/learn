# -*- coding: utf-8 -*-
# from odoo import http


# class Sk(http.Controller):
#     @http.route('/sk/sk', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sk/sk/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sk.listing', {
#             'root': '/sk/sk',
#             'objects': http.request.env['sk.sk'].search([]),
#         })

#     @http.route('/sk/sk/objects/<model("sk.sk"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sk.object', {
#             'object': obj
#         })
