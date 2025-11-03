from odoo import models, fields, api


class QuestionResponse(models.Model):
    _name = 'simple.question_response'
    _description = 'Individual Answer'
    response_text = fields.Char(string="Response Text", required=True)
    phone_number = fields.Char(string="Phone Number")
    question = fields.Many2one('simple.question')
    survey = fields.Many2one('simple.response')
    # @api.depends('question.name', 'response_text')
    # def _compute_display_text(self):
    #    for record in self:
    #        record.display_text = record.question.name + ": " + record.response_text


class SimpleResponse(models.Model):
    _name = 'simple.response'
    _description = 'Survey Response'

    phone_number = fields.Char(string='Phone Number', required=True)
    responses = fields.One2many(
        'simple.question_response', 'survey', string='Survey Response')
    survey = fields.Many2one('simple.survey', string='Survey')
