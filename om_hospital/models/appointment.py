from odoo import fields, models, api

class HospitalPatient(models.Model):
    _name = 'appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Janji Temu'
    
    name = fields.Char(string='Janji Temu')
    pasien_id = fields.Many2one(comodel_name='hospital.patient', string='Pasien')
    jenis_kel = fields.Selection(related='pasien_id.jenis_kel')
    waktu = fields.Datetime('jam')
    tanggal = fields.Date(string='Tanggal')
    
    
    
    
    
