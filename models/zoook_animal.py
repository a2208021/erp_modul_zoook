from odoo import models, fields     
class zoook_animal(models.Model): 
    _name = 'zoook.animal' 
    name = fields.Char(compute='_get_name', string="Id", readonly='True', store=False)
    continentOrigen = fields.Char('Continente de origen', size=100, required=True) 
    paisOrigen = fields.Char('Pais de origen', size=100, required=True)     
    dataNaix = fields.Datetime('Fecha de nacimiento', required=True)     
    sexe = fields.Char('Sexo', size=5, required=True)
    zoo_id = fields.Many2one('zoook.zoo', string='Zoo_id')
    especie_id = fields.Many2one('zoook.especie', string='Especie_id')

    def _get_name(self):
        for r in self:
            r.name = str(r.id)

# El sexo del animal es M y F.