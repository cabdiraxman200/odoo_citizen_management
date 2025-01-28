from odoo import api, fields, models

# District Model
class District(models.Model):
    _name = 'citizen.district'
    _description = 'District'
    name = fields.Char(string='District Name', required=True)
    description = fields.Text(string='Description')
    region_id = fields.Many2one('citizen.region', string='Region', required=True)

