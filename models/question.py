from odoo import models, fields


class SimpleQuestion(models.Model):
    _name = 'simple.question'
    _description = 'Survey Question'

    name = fields.Char(string='Question', required=True)
