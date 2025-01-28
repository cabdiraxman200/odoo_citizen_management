from odoo import api, fields, models
# State Model
class State(models.Model):
    _name = 'citizen.state'
    _description = 'State'
    name = fields.Char(string='State Name', required=True)
    description = fields.Char(string='Description')