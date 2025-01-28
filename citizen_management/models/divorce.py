from odoo import models, fields, api


class Divorce(models.Model):
    _name = 'citizen.divorce'
    _description = 'Divorce Record'

    citizen_id = fields.Many2one(
        'citizen.citizen',
        string='Man Who Divorced',
        required=True,
        ondelete='cascade',
        domain=[('gender', '=', 'male'), ('status', '=', 1), ('marital_status', '=', 'married')]
    )
    woman_divorce = fields.Many2one(
        'citizen.citizen',
        string='Woman Divorced',
        required=True,
        ondelete='cascade',
        domain=[('gender', '=', 'female'), ('status', '=', 1), ('marital_status', '=', 'married')]
    )
    witness_one = fields.Char(string='Witness One', required=True)
    witness_two = fields.Char(string='Witness Two', required=True)
    dowry = fields.Many2one(
        'citizen.marriage',
        string='Dowry',
        required=True,
        ondelete='cascade'
    )
    dowry_value = fields.Char(
        string='Dowry',
        related='dowry.dowry',  # Directly access the dowry field from the Marriage model
        store=True,
        readonly=True
    )

    divorce_date = fields.Date(string='Divorce Date', required=True)
    reason = fields.Char(string='Reason', required=True)
    divorce_of_money = fields.Float(
        string='Divorce Amount',
        compute='_compute_divorce_fee',
        store=True,
        readonly=False,
    )

    @api.depends('citizen_id')
    def _compute_divorce_fee(self):
        """Compute divorce fee from the Invoice model or use a default value."""
        for record in self:
            invoice = self.env['citizen.invoice'].search([('type', '=', 'divorce')], limit=1)
            record.divorce_of_money = invoice.amount if invoice else 35.0


    @api.model
    def create(self, vals):
        """Override the create method to update marital_status for groom and bride."""
        divorce = super(Divorce, self).create(vals)
        # Update marital_status for the groom
        if divorce.citizen_id:
            divorce.citizen_id.write({'marital_status': 'divorced'})
        # Update marital_status for the bride
        if divorce.woman_divorce:
            divorce.woman_divorce.write({'marital_status': 'divorced'})
        return divorce
