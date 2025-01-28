from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
class Citizen(models.Model):
    _name = 'citizen.citizen'
    _description = 'Citizen'
    _rec_name = 'name'
    name = fields.Char(string="Name", required=True, unique=True)
    phone = fields.Char(string="Phone", required=True, unique=True)
    email = fields.Char(string="Email", required=True, unique=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        string="Gender",
        required=True
    )
    job = fields.Char(string="Job", required=True)
    national_id = fields.Char(string="National ID", default='New')
    birth_date = fields.Date(string="Birth Date", required=True)
    # Relationships
    state_id = fields.Many2one('citizen.state', string="State")
    region_id = fields.Many2one('citizen.region', string="Region")  # Custom Region model
    district_id = fields.Many2one('citizen.district', string="District")  # Custom District model
    # Marital Status
    marital_status = fields.Selection(
        [('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')],
        string="Marital Status",
        required=True
    )
    # Status Field
    status = fields.Integer(string="Status", default=1)
    # Constraints for validation
    @api.constrains('email')
    def _check_email_format(self):
        """Validate that the email is in the correct format."""
        email_regex = r'^[^@]+@[^@]+\.[^@]+$'
        for record in self:
            if not re.match(email_regex, record.email):
                raise ValidationError("The email '%s' is not valid." % record.email)

    @api.constrains('phone', 'email', 'national_id')
    def _check_unique_fields(self):
        """Ensure that phone, email, and national_id are unique."""
        for record in self:
            # Check if another record exists with the same phone, email, or national_id
            if self.search_count([('id', '!=', record.id), ('phone', '=', record.phone)]):
                raise ValidationError("The phone '%s' is already registered." % record.phone)
            if self.search_count([('id', '!=', record.id), ('email', '=', record.email)]):
                raise ValidationError("The email '%s' is already registered." % record.email)
            if self.search_count([('id', '!=', record.id), ('national_id', '=', record.national_id)]):
                raise ValidationError("The National ID '%s' is already registered." % record.national_id)
    @api.model_create_multi
    def create(self,vals_list):
          for vals in vals_list:
              if not vals.get('national_id') or vals['national_id'] =='New':
                  vals['national_id']=self.env['ir.sequence'].next_by_code('citizen.citizen')
          return super().create(vals_list)
