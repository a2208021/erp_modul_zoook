from odoo import models, fields     
class zoook_especie(models.Model): 
    _name = 'zoook.especie' 
    nomVulgar = fields.Char('Nombre común', required=True) 
    nomCientific = fields.Char('Nombre científico', required=True)     
    familia = fields.Char('Familia', required=True)     
    perill = fields.Integer('Estado de peligro', required=True)

# El campo perill es un Integer que indica en peligro si es 1
# y lo contrario si es 0.