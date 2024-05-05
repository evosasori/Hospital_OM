from odoo import models, fields, api

class Instruktur(models.Model):
    _name = 'instruktur'
    _description = 'Instruktur'
    _inherits = {'res.partner': 'partner_id'}
    
    partner_id      = fields.Many2one(comodel_name='res.partner', string='Partner', required=True, ondelete='cascade')
    keahlian_ids    = fields.Many2many(comodel_name='keahlian', string='Keahlian')
    jabatan_id = fields.Many2one(comodel_name='jabatan', string='ID Jabatan')
    jenis_jabatan = fields.Selection(string='Jenis', related='jabatan_id.jenis_jabatan')
    # kepala_count = fields.Integer(string='Jumlah Kepala', compute='_compute_kepala_count')
    # if (jabatan_id == 'staff'):
    jabatan_staff = fields.Char(string='Nama Staff Jabatan')
    # else :
    #     jabatan_staff = False
    # @api.depends('jenis_jabatan')
    # def _compute_kepala_count(self):
    #     for instruktur in self:
    #         if instruktur.jenis_jabatan == 'kepala':
    #             instruktur.kepala_count = 1
    #         else:
    #             instruktur.kepala_count = 0  
    def action_update_jabatan(self):
        if self.env.context.get('jenis_jabatan') == 'kepala':
            return False
        self.jabatan_id.pejabat = self.id
        
        return {
            'name': 'Jabatan',
            'type': 'ir.actions.act_window',
            'res_model': 'jabatan',
            'view_mode': 'tree',
            'target': 'current',
        }
    
class Keahlian(models.Model):
    _name           = 'keahlian'
    _description    = 'Keahlian'

    name = fields.Char(string='Nama Keahlian', required=True)