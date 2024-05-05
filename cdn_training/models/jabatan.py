from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Jabatan1(models.Model):
    _name = 'jabatan'
    _description = 'Jabatan'
    
    name = fields.Char(string='Nama Jabatan')
    jenis_jabatan = fields.Selection(string='Jenis Jabatan', selection=[('kepala', 'Kepala/Pimpinan Lembaga'), ('wakil', 'Wakil Lembaga'),('staff', 'Staff Lembaga'),])
    keterangan = fields.Text(string='Keterangan')
    pejabat = fields.Many2one(comodel_name='instruktur', string='Nama Pejabat', readonly=True)
    
    @api.constrains('jenis_jabatan')
    def _check_jabatan_constraints(self):
        for record in self:
            if record.jenis_jabatan == 'kepala':
                existing_kepala = self.search([('jenis_jabatan', '=', 'kepala')])
                if len(existing_kepala) > 1 or (len(existing_kepala) == 1 and existing_kepala.id != record.id):
                    raise ValidationError("Hanya boleh ada satu Kepala / Pimpinan Lembaga.")
            elif record.jenis_jabatan == 'wakil':
                existing_wakil = self.search([('jenis_jabatan', '=', 'wakil')])
                if len(existing_wakil) > 1 or (len(existing_wakil) == 1 and existing_wakil.id != record.id):
                    raise ValidationError("Hanya boleh ada satu Wakil Kepala Lembaga.")  

    