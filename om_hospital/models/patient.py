from odoo import fields, models, api
from datetime import date

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    
    name = fields.Char(string='Nama Pasien',tracking=True, default="pasien")
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    umur = fields.Integer(string='Umur',compute='_compute_usia', tracking=True, help='Otomatis terisi saat mengganti tanggal lahir')
    ref = fields.Char(string='Referensi',tracking=True) 
    jenis_kel = fields.Selection(string='Jenis Kelamin', selection=[('laki', 'Laki - Laki'), ('perempuan', 'Perempuan'),],tracking=True)
    active = fields.Boolean(string="aktif", default="True",tracking=True)
    # janji_id = fields.Many2one(comodel_name='appointment', string='Janji')
    
    
    @api.depends('tanggal_lahir')
    def _compute_usia(self):
        for rec in self:
            today = date.today()
            if rec.tanggal_lahir:
                rec.umur = today.year - rec.tanggal_lahir.year
            else :
                rec.umur = 0    
    
    
