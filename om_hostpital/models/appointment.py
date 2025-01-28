# -*- coding: utf-8 -*-
from odoo import api, fields, models
class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection(string="Gender", related="patient_id.gender", readonly=False)
    appointment_date = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date("Booking_Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference")
    doctor_id = fields.Many2one('res.users', string='Doctor')
    prescription = fields.Html(string="Prescription")
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines','appointment_id',string='Pharmacy',)
    hide_sales_price = fields.Boolean(string="Hide Sales Price")
    priority = fields.Selection([
        ('0', 'normal'),
        ('1', 'low'),
        ('2', 'high'),
        ('3', 'very high')])
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string='Status')

    def test_action(self):
        print("clicked...")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'click successfully',
                'type': 'rainbow_man'
            }
        }

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        action = self.env.ref('om_hostpital.action_cancel_appointment').read()[0]
        return action

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

class AppointmentPharmacy(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = 'Appointment Pharmacy lines'
    product_id = fields.Many2one('product.product', string='Product')
    price_unit = fields.Float( related='product_id.list_price',string='Price')
    qty = fields.Integer(string='Quantity',default=1)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
