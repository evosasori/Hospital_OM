from odoo import models, fields, api



class Peserta(models.Model):
    _name = 'peserta'
    _description = 'Peserta'
    _inherits = {'res.partner': 'partner_id'}
    
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner ID', required=True, ondelete='cascade')
    pendidikan = fields.Selection([('smp', 'SMP'),('sma', 'SMK/SMA'),('diploma', 'D1/D2/D3'),('s1', 'S1'),('s1', 'S2'),], string='Pendidikan')
    pekerjaan = fields.Char(string='Pekerjaan')
    is_menikah = fields.Boolean(string='Menikah', default=False)
    nama_pasangan = fields.Char(string='Nama Istri/Suami')
    hp_pasangan = fields.Char(string='No HP Istri/Suami')
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    
    
    
    
    
    
