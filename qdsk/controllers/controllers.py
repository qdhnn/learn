# -*- coding: utf-8 -*-
# from odoo import http


# class Qdsk(http.Controller):
#     @http.route('/qdsk/qdsk', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qdsk/qdsk/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qdsk.listing', {
#             'root': '/qdsk/qdsk',
#             'objects': http.request.env['qdsk.qdsk'].search([]),
#         })

#     @http.route('/qdsk/qdsk/objects/<model("qdsk.qdsk"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qdsk.object', {
#             'object': obj
#         })
