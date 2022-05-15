# -*- coding: utf-8 -*-
# from odoo import http


# class Geekmeet(http.Controller):
#     @http.route('/geekmeet/geekmeet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/geekmeet/geekmeet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('geekmeet.listing', {
#             'root': '/geekmeet/geekmeet',
#             'objects': http.request.env['geekmeet.geekmeet'].search([]),
#         })

#     @http.route('/geekmeet/geekmeet/objects/<model("geekmeet.geekmeet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('geekmeet.object', {
#             'object': obj
#         })
