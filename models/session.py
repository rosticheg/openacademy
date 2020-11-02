# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'openacademy_session'

    name = fields.Char(string='Session', required=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done')], required=True, default='draft', tracking=True)
    start_date = fields.Date("Start Date", default=fields.Date.today)
    stop_date = fields.Date("Stop Date", default=fields.Date.today)
    duration = fields.Float(digits=(6,2), help="Duration in days")
    instructor_id = fields.Many2one('openacademy.partner')
    course_id = fields.Many2one('openacademy.course', ondelete="cascade", string="Course", required = True)
    attende_ids = fields.Many2many('openacademy.partner')
    active = fields.Boolean(default=True)