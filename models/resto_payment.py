# resto/models/resto_payment.py
from odoo import models, fields, api

class RestoPayment(models.Model):
    _name = 'resto.payment'
    _description = 'Resto Payment'

    order_id = fields.Many2one('resto.order', string='Order Reference', required=True)
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('e_wallet', 'E-Wallet')
    ], string='Payment Method', required=True)
    amount_due = fields.Float(string='Amount Due', related='order_id.total_amount', readonly=True)
    amount_paid = fields.Float(string='Amount Paid', required=True)
    payment_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('partial', 'Partially Paid'),
        ('paid', 'Paid')
    ], string='Payment Status', compute='_compute_payment_status', store=True)

    @api.depends('amount_due', 'amount_paid')
    def _compute_payment_status(self):
        for payment in self:
            if payment.amount_paid >= payment.amount_due:
                payment.payment_status = 'paid'
            elif payment.amount_paid > 0:
                payment.payment_status = 'partial'
            else:
                payment.payment_status = 'unpaid'
