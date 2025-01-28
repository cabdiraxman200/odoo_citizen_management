from odoo import models, fields
class Invoice(models.Model):
    _name = 'citizen.invoice'
    _description = 'Invoice'

    type = fields.Selection([
        ('marriage', 'Marriage'),
        ('Divorce', 'divorce'),
        ('birth', 'Birth'),
        ('death', 'Death'),

    ], required=True, string='Type')
    birth_of_money = fields.Float(
        string='Birth Fee',
        default=25
    )
    marriage_of_money = fields.Float(
        string='Marriage Fee',
        default=30
    )
    divorce_of_money = fields.Float(
        string='Marriage Fee',
        default=35
    )
    death_of_money = fields.Float(
        string='Death Fee',
        default=20
    )

