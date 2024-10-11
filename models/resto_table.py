# resto/models/resto_table.py
from odoo import models, fields, api

class RestoTable(models.Model):
    _name = 'resto.table'
    _description = 'Resto Table'

    table_number = fields.Char(string='Table Number', required=True)
    capacity = fields.Integer(string='Capacity', required=True)
    status = fields.Selection([
        ('empty', 'Empty'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved')
    ], string='Status', default='empty')

    def set_reserved(self):
        """Set the table status to reserved"""
        self.status = 'reserved'

    def set_occupied(self):
        """Set the table status to occupied"""
        self.status = 'occupied'

    def set_empty(self):
        """Set the table status to empty"""
        self.status = 'empty'
