from odoo import models, fields, api

class RestoOrder(models.Model):
    _name = 'resto.order'
    _description = 'Resto Order'

    name = fields.Char(
        string='Order Reference', 
        required=True, 
        copy=False, 
        readonly=True, 
        default=lambda self: self.env['ir.sequence'].next_by_code('resto.order') or 'New'
    )
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    date_order = fields.Datetime(string='Order Date', default=fields.Datetime.now)
    order_line_ids = fields.One2many('resto.order.line', 'order_id', string='Order Lines')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='Status', default='draft')

    # New fields added
    delivery_date = fields.Datetime(string='Scheduled Delivery Date')
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('credit_card', 'Credit Card'),
    ], string='Payment Method')
    tracking_number = fields.Char(string='Tracking Number')
    notes = fields.Text(string='Notes')
    
    @api.depends('order_line_ids.price_total')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.price_total for line in order.order_line_ids)

    def action_confirm(self):
        self.status = 'confirmed'

    def action_done(self):
        self.status = 'done'


class RestoOrderLine(models.Model):
    _name = 'resto.order.line'
    _description = 'Resto Order Line'

    order_id = fields.Many2one('resto.order', string='Order Reference', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    price_unit = fields.Float(string='Unit Price', store=True, readonly=False)
    product_qty = fields.Integer(string='Quantity', default=1)
    price_total = fields.Float(string='Total', compute='_compute_price_total', store=True)
    is_archived = fields.Boolean(string='Archived', default=False)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        """Mengisi otomatis harga unit dari harga produk yang dipilih."""
        for line in self:
            if line.product_id:
                line.price_unit = line.product_id.list_price

    @api.depends('price_unit', 'product_qty')
    def _compute_price_total(self):
        """Menghitung total harga berdasarkan harga unit dan jumlah produk."""
        for line in self:
            line.price_total = line.price_unit * line.product_qty

    def action_archive(self):
        for line in self:
            line.is_archived = True
