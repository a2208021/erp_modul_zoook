from odoo import models, fields     
class zoook_zoo(models.Model): 
    _name = 'zoook.zoo' 
    name = fields.Char(compute='_get_name', string="Nom", readonly='True', store=False)
    nom = fields.Char('Nombre', required=True) 
    pais = fields.Char('Pais', required=True)     
    ciutat = fields.Char('Ciudad', required=True)     
    grandaria = fields.Float('Tamaño', required=True)
    animals_ids = fields.One2many('zoook.animal', 'zoo_id', string='Animals')

    def _get_name(self):
        for r in self:
            r.name = str(r.nom)