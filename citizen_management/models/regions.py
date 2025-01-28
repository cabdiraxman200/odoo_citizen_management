from odoo import  api,models, fields
class Region(models.Model):
    _name = 'citizen.region'
    _description = 'Region'
    name = fields.Char(string='Region Name', required=True)
    description = fields.Text(string='Description')
    state_id = fields.Many2one('citizen.state', string='State', required=True)