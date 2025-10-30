from odoo import models, fields


class Question(models.Model):

    _name = "Question"
    name = fields.Char("Name", required=True)
    questionText = fields.Char()


class Survey(models.Model):
    _name = "Survey"
    name = fields.Char("Name", required=True)
    description = fields.Char("Application Description")
    estimatedCost = fields.Float("Estimated Cost")
