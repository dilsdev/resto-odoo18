from odoo import models, fields

class RestoReservation(models.Model):
    _name = 'resto.reservation'
    _description = 'Resto Reservation'

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    table_id = fields.Many2one('resto.table', string='Reserved Table')
    reservation_date = fields.Datetime(string='Reservation Date and Time', required=True)
    status = fields.Selection([
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='confirmed')

    phone_number = fields.Char(string='Customer Phone Number')
    email = fields.Char(string='Customer Email')
    guest_count = fields.Integer(string='Number of Guests', required=True)
    special_request = fields.Text(string='Special Requests')
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user)
    note = fields.Text(string='Internal Notes')

    def action_confirm(self):
        """Set reservation status to confirmed"""
        self.status = 'confirmed'

    def action_cancel(self):
        """Set reservation status to cancelled"""
        self.status = 'cancelled'
