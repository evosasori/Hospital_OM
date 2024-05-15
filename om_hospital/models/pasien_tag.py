from odoo import api,models, fields,_

class PasienTag(models.Model):
    _name = 'pasien.tag'
    _description = 'Pasien Tag'
    _sql_constraints = [
        ('unique_name', 'Unique(name)','Nama tag sudah ada!'),
        ('check_sequence', 'Check(sequence > 0)','sequence harus Lebih dari 0')
    ]
    name = fields.Char(string='Nama', required=True)
    active = fields.Boolean(string='Aktif', default="True")
    warna = fields.Integer(string='Warna')
    warna2 = fields.Char(string='Warna 2')
    sequence = fields.Integer(string='Urutan')
    
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default={}
        
        if not default.get('name'):
            default['name'] = _("%s (salin)", self.name)
        return super(PasienTag, self).copy(default)
    
    
    
    
     
    
