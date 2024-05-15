from datetime import date
import datetime 
from odoo import  api, fields, models,_
from odoo.exceptions import ValidationError
from dateutil import relativedelta

class BatalTemuWizard(models.TransientModel):
    _name = 'batal.temu.wizard'
    _description = 'Batal Temu Wizard'
    
    appointment_id = fields.Many2one(comodel_name='appointment', string='Janji Temu', domain=[('state', '=', 'draft'),('priority', 'in', ('0','1',False))])
    alasan = fields.Text('alasan')
    date_cancel = fields.Date(string='tanggal Pembatalan')
    
    @api.model
    def default_get(self, fields):
        print(fields)
        res = super(BatalTemuWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        # res['appointment_id'] = self.env.context.get('active_id')
        return res
    
    def aksi_batal(self):
        cancel_day = self.env['ir.config_parameter'].get_param('om_hospital.cancel_days')
        today = date.today()
        allowed = self.appointment_id.tanggal - relativedelta.relativedelta(days=int(cancel_day))
        if allowed < today:
            # 2024-05-12 < 2024-05-15
            print("Allowed", allowed)
            print("Date saat Ini",today)
            raise ValidationError(_("Sorry, the cancellation is not allowed in this time"))
        else:
            raise ValidationError(_("Dua, the cancellation is not allowed in this time"))
        # return
        # for rec in self:
        #     rec.appointment_id.state = "batal"
    
