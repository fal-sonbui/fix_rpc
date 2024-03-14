from odoo import models

class StockQuant(models.Model):
    _inherit = "stock.quant"
    def action_apply_inventory(self):
        return True
