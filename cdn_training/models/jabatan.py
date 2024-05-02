from odoo import models, fields, api


class Jabatan1(models.Model):
    _name = 'jabatan'
    _description = 'Jabatan'
    
    name = fields.Char(string='Nama Jabatan')
    jenis_jabatan = fields.Selection(string='Jenis Jabatan', selection=[('kepala', 'Kepala/Pimpinan Lembaga'), ('wakil', 'Wakil Lembaga'),('staff', 'Staff Lembaga'),])
    keterangan = fields.Text(string='Keterangan')
    pejabat = fields.Many2one(comodel_name='instruktur', string='Nama Pejabat', readonly=True)    

    