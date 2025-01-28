from odoo import models, fields, api
class Birth(models.Model):
    _name = 'citizen.birth'
    _description = 'Birth Record'

    # Reference to Citizen model for the child
    citizen_id = fields.Many2one(
        'citizen.citizen',
        string='Person',
        required=True,
        ondelete='cascade',
    domain = [('status', '=', 1)]
    )
    birth_date = fields.Date(
        string="Birth Date",
        related='citizen_id.birth_date',
        readonly=False
    )
    # Reference to District model for place of birth
    place_of_birth_id = fields.Many2one(
        'citizen.district',
        string='Place of Birth',
        required=True,
        ondelete='cascade'
    )
    # Field to display the Birth Fee dynamically from the Invoice model
    birth_of_money = fields.Float(
        string='Birth Fee',
        compute='_compute_birth_fee',
        store=True,
        readonly=False,
    )

    @api.depends('citizen_id')  # Trigger computation when citizen_id changes
    def _compute_birth_fee(self):
        """Compute the birth fee dynamically from the Invoice model."""
        for record in self:
            # Search for an Invoice record of type 'birth'
            invoice = self.env['citizen.invoice'].search([('type', '=', 'birth')], limit=1)
            # Use the fee from the invoice or fall back to the default value
            record.birth_of_money = invoice.birth_of_money if invoice else 0.0
