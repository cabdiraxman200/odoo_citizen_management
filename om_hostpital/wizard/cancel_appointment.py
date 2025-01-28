
from odoo import api, fields, models
class CancelAppointment(models.TransientModel):
    _name = 'cancel.appointment.wizard'
    _description = 'Cancel Appointment wizard'
    appointment_id = fields.Many2one("hospital.appointment",string='Appointment')
    reason = fields.Text(string='Reason')
    def action_cancel(self):
        return


