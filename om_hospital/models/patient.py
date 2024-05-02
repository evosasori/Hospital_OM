from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    
    name = fields.Char(string='Nama Pasien',tracking=True, default="pasien")
    umur = fields.Integer(string='Umur',tracking=True)
    ref = fields.Char(string='Referensi',tracking=True)
    jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('laki', 'Laki - Laki'), ('perempuan', 'Perempuan'),],tracking=True)
    active = fields.Boolean(string="aktif", default="True",tracking=True)
    
    
    
