from odoo import models,fields,api


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    
    confirmed_user_id = fields.Many2one(comodel_name='res.users', string='Confirmed User')
    
    def action_confirm(self):
        super(SaleOrderInherit,self).action_confirm()
        print("Berhasil.........................................")
        self.confirmed_user_id = self.env.user.id
    
