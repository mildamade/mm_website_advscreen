# -*- coding: utf-8 -*-
from odoo import http

class MmWebsiteAdvscreen(http.Controller):
    @http.route('/mm_website_advscreen/mm_website_advscreen/', auth='public')
    def index(self, **kw):
        Product = http.request.env['product.product']

        return http.request.render('mm_website_advscreen.index', {
            'product': Product.search([['active', '=', True]]),
        })

    @http.route('/mm_website_advscreen/screen1/', auth='public')
    def index1(self, **kw):
        Product = http.request.env['product.product']

        return http.request.render('mm_website_advscreen.index1', {
            'product': Product.search([ ['categ_id', '=', 'Screen 1'],['active', '=', True]],limit=6 , order='__last_update asc'),
        })
    
        
    @http.route('/mm_website_advscreen/screen2/', auth='public')
    def index2(self, **kw):
        Product = http.request.env['product.product']

        return http.request.render('mm_website_advscreen.index2', {
            'product': Product.search([ ['categ_id', '=', 'Screen 2'], ['active', '=', True]],limit=6, order='__last_update asc'),
        })

    @http.route('/mm_website_advscreen/screen3/', auth='public')
    def index3(self, **kw):
        Product = http.request.env['product.product']

        return http.request.render('mm_website_advscreen.index3', {
            'product': Product.search([ ['categ_id', '=', 'Screen 3'], ['active', '=', True]],limit=6,  order='__last_update asc'),
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