from odoo import models, fields


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'The Real Estate Property Tag'

    name = fields.Char('Name', required=True)
    sequence = fields.Integer('Sequence', default=0)
