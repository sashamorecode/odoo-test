from odoo import models, fields, api


class Question(models.Model):

    _name = "odoo_test.question"
    _description = "Question"
    name = fields.Char(string="Name", required=True)
    questionText = fields.Char()


class Survey(models.Model):
    _name = "odoo_test.survey"
    _description = "Survey"
    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Application Description")
    estimatedCost = fields.Float(string="Estimated Cost")
    questions = fields.Many2many("odoo_test.question", string="Questions")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('seeking_approval', 'Seeking Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')], string='Status')
