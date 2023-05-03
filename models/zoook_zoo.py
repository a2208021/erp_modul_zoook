from odoo import models, fields     
class zoook_zoo(models.Model): 
    _name = 'zoook.zoo' 
    nom = fields.Char('Nombre', required=True) 
    pais = fields.Char('Pais', required=True)     
    ciutat = fields.Char('Ciudad', required=True)     
    grandaria = fields.Float('Tamaño', required=True)