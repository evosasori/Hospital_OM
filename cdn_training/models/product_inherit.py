from odoo import models,fields, api



class ProductProduct(models.Model):
    _inherit = 'product.product'
    product_training = fields.Selection(string='jenis Product', selection=[('non_traning', 'Non Traning'), ('konsumsi', 'Konsumsi'),('training_kit', 'Peralatan Training'),], default="non_traning")
    


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    product_training = fields.Selection(string='jenis Product', selection=[('non_traning', 'Non Traning'), ('konsumsi', 'Konsumsi'),('training_kit', 'Peralatan Training'),], default="non_traning")
    