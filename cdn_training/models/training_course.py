from odoo import models, fields, api
from datetime import timedelta

class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Tabel Training Course'
    _sql_constraints = [('name_course_unique', 'Unique(name)', 'Nama Kursus Sudah Ada!')]
    
    name = fields.Char(string='Nama Kursus', required=True)
    description = fields.Text(string='Keterangan')
    user_id = fields.Many2one(comodel_name='res.users', string='Penanggung Jawab')
    session_line = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Sesi Training')
    product_ids = fields.Many2many(comodel_name='product.product', string='Peralatan/Konsumsi', domain=[('product_training','!=','non_training')])
    
    
    
    
class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
        
    name = fields.Char(string='Sesi Training', required=True, tracking=True)
    course_id = fields.Many2one(comodel_name='training.course', string='ID Kursus', required=True, ondelete='cascade', tracking=True)
    start_date = fields.Date(string='Tanggal Mulai', required=True, tracking=True)
    duration = fields.Float(string='Durasi', required=True, tracking=True)
    seats = fields.Integer(string='Max Peserta', required=True, default=1, tracking=True)
    instruktur_id = fields.Many2one(comodel_name='instruktur', string='Nama Instruktur', tracking=True)
    
    alamat = fields.Char(string='Alamat',related='instruktur_id.street', tracking=True)
    no_hp = fields.Char(string='Handphone',related='instruktur_id.mobile', tracking=True)
    email = fields.Char(string='Email',related='instruktur_id.email', tracking=True)
    jenis_kel = fields.Selection(related='instruktur_id.jenis_kel', tracking=True)
    peserta_ids = fields.Many2many(comodel_name='peserta', string='Peserta')
    jml_peserta = fields.Integer(compute='_compute_jml_peserta', string='Jumlah Peserta', tracking=True)
    state  = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('progress', 'Sedang Berlangsung'),('done', 'Selesai')], default='draft', tracking=True)
    end_date = fields.Date(compute='_compute_end_date', string='End Date')
    
    
    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for rec in self :
            days = timedelta(days=rec.duration)
            rec.end_date = rec.start_date + days
    
    @api.depends('peserta_ids')
    def _compute_jml_peserta(self):
        for rec in self:
            rec.jml_peserta = len(rec.peserta_ids)
            
    def action_confirm(self):
        self.state = 'progress'
        
    def action_done(self):
        self.state = 'done'
    
    def action_draft(self):
        self.state = 'draft'