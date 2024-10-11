# resto/models/resto_report.py
from odoo import models, fields, api

class RestoReport(models.TransientModel):
    _name = 'resto.report'
    _description = 'Resto Report'

    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    report_type = fields.Selection([
        ('sales', 'Sales'),
        ('payment', 'Payment'),
    ], string='Report Type', required=True)

    def generate_report(self):
        """
        This function generates the report based on the selected filters
        and redirects to the report view.
        """
        if self.report_type == 'sales':
            return self._generate_sales_report()
        elif self.report_type == 'payment':
            return self._generate_payment_report()

    def _generate_sales_report(self):
        # Logic to generate sales report
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sales Report',
            'res_model': 'resto.order',
            'view_mode': 'tree',
            'domain': [('date_order', '>=', self.start_date), ('date_order', '<=', self.end_date)],
        }

    def _generate_payment_report(self):
        # Logic to generate payment report
        return {
            'type': 'ir.actions.act_window',
            'name': 'Payment Report',
            'res_model': 'resto.payment',
            'view_mode': 'tree',
            'domain': [('create_date', '>=', self.start_date), ('create_date', '<=', self.end_date)],
        }
