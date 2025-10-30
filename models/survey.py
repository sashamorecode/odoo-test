from odoo import models, fields, api


class SimpleSurvey(models.Model):
    _name = 'simple.survey'
    _description = 'Simple Survey'

    name = fields.Char(string='Survey Title', required=True)
    description = fields.Text(string='Description')
    estimated_costs = fields.Float(string='Estimated Costs')
    phone_numbers_file = fields.Binary(string='Upload Phone Numbers (CSV)')
    question_ids = fields.Many2many(
        'simple.question',
        string='Questions',
        relation='survey_question_rel',
        column1='survey_id',
        column2='question_id'
    )
