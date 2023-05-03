from odoo import models, fields     
class zoook_animal(models.Model): 
    _name = 'zoook.animal' 
    continentOrigen = fields.Char('Continente de origen', required=True) 
    paisOrigen = fields.Char('Pais de origen', required=True)     
    dataNaix = fields.Char('Fecha de nacimiento', required=True)     
    sexe = fields.Char('Sexo', required=True)

# El sexo del animal es M y F.