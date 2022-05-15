# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.modules.module import get_module_resource
import base64
from dateutil.relativedelta import *
from datetime import date, datetime


class Movie(models.Model):
    _name = 'geekmeet.movie'
    _description = 'Movie\'s database'
    _order = 'date_publish'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('geekmeet', 'static/src/img', 'default_movie.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char(size=32, string='Movie\'s name',required=True, index=True)
    date_publish = fields.Date('Publish date')
    cover = fields.Image(default=_default_image)
    director_id = fields.Many2one('geekmeet.director','Director')
    producer_id = fields.Many2one('geekmeet.producer','Producer')
    description = fields.Text()
    active = fields.Boolean('Active', default=True)
    creator_id = fields.Many2one('res.users','Created by',default=lambda self: self.env.user)
    comment_ids = fields.One2many('geekmeet.comment','movie_id','Comments')

class Director(models.Model):
    _name = 'geekmeet.director'
    _description = 'Director\'s database'
    _order = 'last_name'
    _inherit = ['image.mixin']

    @api.model
    def _default_image(self):
        image_path = get_module_resource('geekmeet', 'static/src/img', 'default_director.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char(size=32, string='Directors\'s name',required=True)
    last_name = fields.Char(size=32, string='Director\'s last name', required=True, index=True)
    image = fields.Image(default=_default_image)
    birthdate = fields.Date('Birthdate')
    is_dead = fields.Boolean('Is dead?')
    deceasedate = fields.Date('Decease date')
    age = fields.Integer('Age', compute='_age_compute', readonly=True)
    movie_ids = fields.One2many('geekmeet.movie','director_id','Movies')

    @api.depends('birthdate','is_dead','birthdate')
    def _age_compute(self):
        today = date.today()
        for record in self:
            if not record.is_dead:
                record.age = relativedelta(today, record.birthdate).years
            else:
                record.age = None

    def name_get(self):
        result = []
        for record in self:
            name = record.name + ' ' + record.last_name
            result.append((record.id, name))
        return result

class Producer(models.Model):
    _name = 'geekmeet.producer'
    _description = 'Producer\'s database'

    name = fields.Char(size=32, string='Producer\'s name')
    movie_ids = fields.One2many('geekmeet.movie','producer_id','Movies')
    description = fields.Text()

class Comment(models.Model):
    _name = 'geekmeet.comment'
    _order = 'datetime_publish'

    @api.model
    def _myself(self):
        return self.env.user

    @api.model
    def _movie(self):
        peli=self.env.context.get('movie_id')
        return peli

    name = fields.Char(size=32, string="Subject")
    datetime_publish = fields.Datetime('Publish date', default=datetime.now())
    movie_id = fields.Many2one('geekmeet.movie', 'Movie', default=_movie)
    creator_id = fields.Many2one('res.users', 'Created by', default=_myself)
    description = fields.Text()
    active = fields.Boolean('Active', default=True)
