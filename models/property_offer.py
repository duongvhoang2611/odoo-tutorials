from odoo import models, fields, api
from datetime import timedelta


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'The Real Estate Property Offer'

    price = fields.Float('Price')
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')], string='Status', copy=False
    )
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    validity = fields.Integer(
        'Validity (Days)',
        compute='_compute_validity',
        inverse='_inverse_validity',
        store=True,
        default=7,
    )
    date_deadline = fields.Date(
        'Date deadline',
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline',
        store=True,
    )

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.validity:
                record.date_deadline = fields.Date.today() + timedelta(
                    days=record.validity
                )

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - fields.Date.today()).days

    @api.depends('date_deadline')
    def _compute_validity(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - fields.Date.today()).days

    def _inverse_validity(self):
        for record in self:
            if record.validity:
                record.date_deadline = fields.Date.today() + timedelta(
                    days=record.validity
                )
