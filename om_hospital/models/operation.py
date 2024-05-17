from odoo import _, api, fields, models

class HospitalOperation(models.Model):
    _name = 'hospital.operation'
    _description = 'Hospital Operation'
    _log_access = False
    # _log_access = True 
    
    dokter_id = fields.Many2one(comodel_name='res.users', string='Dokter')
    nama_operasi = fields.Char(string='Nama Operasi')
    reference_record = fields.Reference(string='Record', selection=[('hospital.patient', 'Pasien'), ('appointment', 'janji Temu'),])
    
    
    
    @api.model
    def name_create(self,name):
        print("value nama --->>>>>>>>>>>>>>>>>>>>>>>>>>", name)
        return self.create({'nama_operasi': name}).name_get()[0]
    
