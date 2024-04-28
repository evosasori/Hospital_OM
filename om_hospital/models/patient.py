from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    
    name = fields.Char(string='Nama Pasien')
    umur = fields.Integer(string='Umur')
    jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('laki', 'Laki - Laki'), ('perempuan', 'Perempuan'),])
    
    
    
