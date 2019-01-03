# -*- coding: utf-8 -*-
from odoo import http

class MmWebsiteAdvscreen(http.Controller):
    @http.route('/mm_website_advscreen/mm_website_advscreen/', auth='public')
    def index(self, **kw):
        Product = http.request.env['product.product']

        return http.request.render('mm_website_advscreen.index', {
            'product': Product.search([]),
        })


#        Product = http.request.env['product.product']
#        return http.request.render('mm_website_advscreen.index', {
#            'product': Product.search([])
#        })

#     @http.route('/mm_website_advscreen/mm_website_advscreen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mm_website_advscreen.listing', {
#             'root': '/mm_website_advscreen/mm_website_advscreen',
#             'objects': http.request.env['mm_website_advscreen.mm_website_advscreen'].search([]),
#         })

#     @http.route('/mm_website_advscreen/mm_website_advscreen/objects/<model("mm_website_advscreen.mm_website_advscreen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mm_website_advscreen.object', {
#             'object': obj
#         })