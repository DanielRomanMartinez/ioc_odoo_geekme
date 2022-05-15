# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class User(models.Model):
    _inherit = 'res.users'

    comment_ids = fields.Many2one('geekmeet.comment')