from odoo import fields, models, api

class HospitalAppointment(models.Model):
    _name = 'appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Janji Temu'
    _rec_name = 'pasien_id'
    
    pasien_id = fields.Many2one(comodel_name='hospital.patient', string='Pasien')
    jenis_kel = fields.Selection(related='pasien_id.jenis_kel')
    waktu = fields.Datetime('jam')
    tanggal = fields.Date(string='Tanggal')
    ref = fields.Char(
        string='Referensi', 
        help="Anda akan diarahkan ke halaman pasien!"
        ) 
    resep = fields.Html(string='Resep Obat')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string='Prioritas')
    
    state = fields.Selection([
        ('draf', 'Draf'),
        ('on_konsultasi', 'Sedang Konsultasi'),
        ('selesai', 'Selesai'),
        ('batal', 'Batal'),
    ], string='Status',default='draft')
    
    @api.onchange('pasien_id')
    def _onchange_pasien_id(self):
        self.ref = self.pasien_id.ref
        
    def action_test(self):
        return {
            'effect' : {
                'fadeout': 'slow',
                'message': 'Tombol Diklik',
                'type': 'rainbow_man'
            }
        }
    
    
    
