from odoo import fields, models, api,_
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'
    
    name = fields.Char(string='Nama Pasien',tracking=True, default="pasien")
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    umur = fields.Integer(string='Umur',compute='_compute_usia', inverse='_inverse_umur', tracking=True, help='Otomatis terisi saat mengganti tanggal lahir',search='_cari_umur')
    ref = fields.Char(string='Referensi') 
    jenis_kel = fields.Selection(
        string='Jenis Kelamin', selection=[
            ('laki', 'Laki - Laki'), ('perempuan', 'Perempuan'),
            ],
        tracking=True, help='Pilih')
    active = fields.Boolean(string="aktif", default="True",tracking=True)
    appointment_id = fields.Many2one(comodel_name='appointment', string='Janji Temu') 
    profil = fields.Image('profil')
    tag_ids = fields.Many2many(comodel_name='pasien.tag', string='Tag')
    jumlah_janji = fields.Integer(compute='_compute_jumlah_janji', string='jumlah janji',store=True)
    appointment_ids = fields.One2many(comodel_name='appointment', inverse_name='pasien_id', string='Banyak Janji Temu')
    parent = fields.Char(string='Orang Tua')
    marital_status = fields.Selection(string='Status Pernikahan', selection=[('married', 'Menikah'), ('single', 'Belum Menikah')],tracking=True, default="single")
    partner_name = fields.Char(string='Nama Pasangan') 
    
    @api.depends('appointment_ids')
    def _compute_jumlah_janji(self):
        for rec in self:
            rec.jumlah_janji = self.env['appointment'].search_count([('pasien_id','=',rec.id)])
    
    @api.constrains('tanggal_lahir')
    def _check_tanggal_lahir(self):
        for rec in self:
            if rec.tanggal_lahir and rec.tanggal_lahir > fields.Date.today():
                raise ValidationError(_("Tanggal Lahir Abnormal"))
    
    @api.model
    def create(self, vals):
        print("Belajar Odoo", vals)
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)
    
    def write(self, vals):
        print(vals)
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)
    
    def name_get(self):
        # for record in self:
        #     patient_list = []
        #     name = '[' + record.ref + ']' + ':' + record.name
        #     patient_list.append((record.id, name))
            
        #     return patient_list
        return [(record.id, "[%s] : %s" % (record.ref, record.name)) for record in self]
    
    @api.depends('tanggal_lahir')
    def _compute_usia(self):
        for rec in self:
            today = date.today()
            if rec.tanggal_lahir:
                rec.umur = today.year - rec.tanggal_lahir.year
            else :
                rec.umur = 0
                
    @api.depends('umur')
    def _inverse_umur(self):
        today = date.today()
        for rec in self:
            rec.tanggal_lahir = today - relativedelta.relativedelta(years=rec.umur)
    
    def _cari_umur(self, operator, value):
        tanggal_lahir = date.today() - relativedelta.relativedelta(years=value)
        start_of_year = tanggal_lahir.replace(day=1,month=1)
        end_of_year = tanggal_lahir.replace(day=31,month=12)
        return [('tanggal_lahir','>=',start_of_year), ('tanggal_lahir','<=',end_of_year)]
        
    @api.ondelete(at_uninstall="False")
    def _check_appointment(self):
        for rec in self:
            if rec.appointment_ids:
             raise ValidationError(_("Tidak Bisa Menghapus Pasien dengan Pertemuan"))
    
    def action_test(self):
        print('Button Clicked')
        return
    
                
                
    
    
