from odoo import models, fields     
class zoook_especie(models.Model): 
    _name = 'zoook.especie' 
    nomVulgar = fields.Char('Nombre común', size=200, required=True) 
    name = fields.Char(compute='_get_name', string="Nom_Vulgar", readonly='True', store=False)
    nomCientific = fields.Char('Nombre científico', size=250, required=True)     
    familia = fields.Char('Familia', size=200, required=True)     
    perill = fields.Integer('Estado de peligro', size=5, required=True)
    animals_ids = fields.One2many('zoook.animal', 'especie_id', string='Animals')

    def _get_name(self):
        for r in self:
            r.name = str(r.nomVulgar)

# El campo perill es un Integer que indica en peligro si es 1
# y lo contrario si es 0.