from odoo import models, fields, api

class QCReport(models.Model):
	_inherit = 'qc.inspection'

	jenis_kertas = fields.Char('Jenis Kertas')
	grammatur = fields.Char('Grammatur')
	panjang = fields.Integer('Panjang')
	lebar = fields.Integer('Lebar')
	tinggi = fields.Integer('Tinggi')
	qty_bundle = fields.Integer('Qty Per Bundle')