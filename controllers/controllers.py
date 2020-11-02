# -*- coding: utf-8 -*-
from odoo import http

# class C:\odoo\openacademy(http.Controller):
#     @http.route('/c:\odoo\openacademy/c:\odoo\openacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\odoo\openacademy/c:\odoo\openacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\odoo\openacademy.listing', {
#             'root': '/c:\odoo\openacademy/c:\odoo\openacademy',
#             'objects': http.request.env['c:\odoo\openacademy.c:\odoo\openacademy'].search([]),
#         })

#     @http.route('/c:\odoo\openacademy/c:\odoo\openacademy/objects/<model("c:\odoo\openacademy.c:\odoo\openacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\odoo\openacademy.object', {
#             'object': obj
#         })