from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = 'appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Janji Temu'
    _order = 'id desc'
    
    name = fields.Char(string='ID Janji')
    pasien_id = fields.Many2one(comodel_name='hospital.patient', string='Pasien',ondelete = "cascade")
    jenis_kel = fields.Selection(related='pasien_id.jenis_kel')
    waktu = fields.Datetime('jam', default=fields.Datetime.now)
    tanggal = fields.Date(string='Tanggal', default=fields.Date.context_today)
    operation_id = fields.Many2one(comodel_name='hospital.operation', string='Operasi')
    
    ref = fields.Char(
        string='Referensi', 
        help="Record referensi !"
        ) 
    resep = fields.Html(string='Resep Obat')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string='Prioritas')
    
    state = fields.Selection([
        ('draft', 'Draf'),
        ('on_konsultasi', 'Sedang Konsultasi'),
        ('selesai', 'Selesai'),
        ('batal', 'Batal'),
    ], string='Status',default='draft')
    dokter_id = fields.Many2one(comodel_name='res.users', string='Dokter')
    
    farmasi_line_ids = fields.One2many(comodel_name='appointment.pharmacy.lines', inverse_name='appointment_id', string='Nama Farmasi')
    sembunyikan_harga = fields.Boolean(string='Sembunyikan Harga')
    
    
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
    
    def action_konsultasi(self):
        for rec in self:
            if rec.state == 'draft':
                rec.state = 'on_konsultasi'
            
    def action_selesai(self):
        for rec in self:
            rec.state = 'selesai'
            
    def action_batal(self):
        action = self.env.ref('om_hospital.batal_temu_wizard_action').read()[0]
        return action
        # for rec in self:
        #     rec.state = 'batal'
    
    def action_draf(self):
        for rec in self:
            rec.state = 'draft'
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('appointment')
        return super(HospitalAppointment, self).create(vals)
    
    def unlink(self):
        print("Test.........................................")
        if self.state == 'selesai':
            raise ValidationError(_("Jika Status 'Selesai', maka tidak bisa dihapus"))
        return super(HospitalAppointment, self).unlink()
            
       


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one(comodel_name='product.product', string='ID Produk', required=True)
    price_unit = fields.Float(related="product_id.lst_price", string='Harga')
    qty = fields.Integer(string='Jumlah', default="1")
    appointment_id = fields.Many2one(comodel_name='appointment', string='Janji')
    
    
    