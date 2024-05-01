from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Instruktur(models.Model):
    _name = 'instruktur'
    _description = 'Instruktur'
    _inherits = {'res.partner': 'partner_id'}
    
    partner_id      = fields.Many2one(comodel_name='res.partner', string='Partner', required=True, ondelete='cascade')
    keahlian_ids    = fields.Many2many(comodel_name='keahlian', string='Keahlian')
    jabatan_id = fields.Many2one(comodel_name='jabatan1', string='ID Jabatan')
    jenis_jabatan = fields.Selection(string='Jenis', related='jabatan_id.jenis_jabatan')
    # if (jabatan_id == 'staff'):
    jabatan_staff = fields.Char(string='Nama Staff Jabatan')
    # else :
    #     jabatan_staff = False
    
class Keahlian(models.Model):
    _name           = 'keahlian'
    _description    = 'Keahlian'

    name = fields.Char(string='Nama Keahlian', required=True)