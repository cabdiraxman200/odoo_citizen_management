from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Patient Master"
    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Reference", help="Reference  from patient")
    _rec_name = 'name'
    date_of_birth = fields.Date(string="DOB", tracking=True)
    age = fields.Integer(string="Age",store=True,compute='_compute_age')
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender", tracking=True, default='female')
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    image= fields.Image(string="Image")
    tag_ids=fields.Many2many('patient.tag',string='Tags')

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:

                # Calculate age based on year difference and adjust for month/day if necessary
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1
