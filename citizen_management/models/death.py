from odoo import models, fields, api
class Death(models.Model):
    _name = 'citizen.death'
    _description = 'Death Record'
    # Reference to Citizen model for the citizen death
    citizen_id = fields.Many2one(
        'citizen.citizen',
        string='Person Death',
        required=True,
        ondelete='cascade',
    domain = [('status', '=', 1)]
    )
    death_date = fields.Date(
        string="Death Date",
        required=True
    )
    # Reference to District model for place of death
    place_of_death = fields.Many2one(
        'citizen.district',
        string='Place of Death',
        required=True,
        ondelete='cascade'
    )
    cause_of_death = fields.Char(string='Cause of Death', required=False)
    # Field to display the Death Fee dynamically from the Invoice model
    death_of_money = fields.Float(
        string='Death Amount',
        compute='_compute_death_fee',
        store=True,
        readonly=False,
    )

    @api.depends('citizen_id')  # Trigger computation when citizen_id changes
    def _compute_death_fee(self):
        """Compute the death fee dynamically from the Invoice model."""
        for record in self:
            # Search for an Invoice record of type 'death'
            invoice = self.env['citizen.invoice'].search([('type', '=', 'death')], limit=1)
            # Use the fee from the invoice or fall back to the default value
            record.death_of_money = invoice.death_of_money if invoice else 20.0

    @api.model
    def create(self, vals):
        """Override create method to update citizen status after death record creation."""
        death_record = super(Death, self).create(vals)
        # Update the citizen's status to 0 (deceased)
        citizen = death_record.citizen_id
        if citizen:
            citizen.write({'status': 0})
        return death_record
