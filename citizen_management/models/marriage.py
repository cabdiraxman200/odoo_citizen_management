from odoo import models, fields, api
from datetime import date
class Marriage(models.Model):
    _name = 'citizen.marriage'
    _description = 'Marriage Record'

    citizen_id = fields.Many2one(
        'citizen.citizen',
        string='Groom',
        required=True,
        ondelete='cascade',
        domain=[('gender', '=', 'male'), ('status', '=', 1)]
    )
    bride = fields.Many2one(
        'citizen.citizen',
        string='Bride',
        required=True,
        ondelete='cascade',
        domain=[
            ('gender', '=', 'female'),
            ('status', '=', 1),
            '|',
            ('marital_status', '=', 'single'),
            ('marital_status', '=', 'divorced'),
            ('birth_date', '<=', date.today().replace(year=date.today().year - 14))  # Age > 14
        ]
    )

    sheikh = fields.Char(string='Sheikh', required=True)
    witness_one = fields.Char(string='Witness One', required=True)
    witness_two = fields.Char(string='Witness Two', required=True)
    marriage_date = fields.Date(string='Marriage Date', required=True)
    location = fields.Char(string='Location', required=True)
    dowry = fields.Char(string='Dowry', required=True)

    # Field to display the Marriage Fee dynamically from the Invoice model
    marriage_of_money = fields.Float(
        string='Marriage Amount',
        compute='_compute_marriage_fee',
        store=True,
        readonly=False,
    )

    @api.depends('citizen_id')  # Trigger computation when citizen_id changes
    def _compute_marriage_fee(self):
        """Compute the marriage fee dynamically from the Invoice model."""
        for record in self:
            # Search for an Invoice record of type 'marriage'
            invoice = self.env['citizen.invoice'].search([('type', '=', 'marriage')], limit=1)
            # Use the amount from the invoice or fall back to a default value
            record.marriage_of_money = invoice.amount if invoice else 30.0

    @api.model
    def create(self, vals):
        """Override the create method to update marital_status for groom and bride."""
        # Create the marriage record
        marriage = super(Marriage, self).create(vals)

        # Update marital_status for groom
        if marriage.citizen_id:
            marriage.citizen_id.write({'marital_status': 'married'})

        # Update marital_status for bride
        if marriage.bride:
            marriage.bride.write({'marital_status': 'married'})

        return marriage
