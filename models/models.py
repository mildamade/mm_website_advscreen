# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import float_round

# class mm_website_advscreen(models.Model):
#     _name = 'mm_website_advscreen.mm_website_advscreen'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100