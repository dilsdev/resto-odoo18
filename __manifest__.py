{
    'name': 'Restaurant Management',
    'version': '1.0',
    'summary': 'Restaurant system for managing menu, orders, and customers',
    'description': """
        A custom module for managing a restaurant's menu, orders, and customers.
    """,
    'category': 'Restaurant',
    'author': 'Your Name',
    'depends': ['base', 'product'],  # Pastikan 'product' diperlukan jika Anda menggunakan produk
    'data': [
        'security/ir.model.access.csv',
        'views/resto_order_views.xml',
        'views/resto_customer_views.xml',
        'views/resto_inventory_views.xml',
        'views/resto_payment_views.xml',
        'views/resto_report_views.xml',
        'views/resto_table_views.xml',
        'views/resto_reservation_views.xml',
    ],
    'sequence': -2,
    'installable': True,
    'application': True,
}
