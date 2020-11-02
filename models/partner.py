# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _name = 'openacademy.partner'
    _description = 'openacademy_partner'

    name = fields.Char(string='Session', required=True)
    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many("openacademy.session", string="Attended Session", readonly = True)