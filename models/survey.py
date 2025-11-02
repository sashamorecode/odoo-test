from odoo import models, fields


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
    approval_state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ])
    approval_state.default = 'draft'

    def action_submit_for_approval(self, *args):
        self.approval_state = 'waiting'

    def action_approve(self, *args):
        # if self.env.user.has_group('manager'):
        self.approval_state = 'approved'

    def action_reject(self, *args):
        self.approval_state = 'rejected'
