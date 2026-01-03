from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Inscription(models.Model):
    _name = 'tp.inscription'
    _description = 'Inscription'

    # =====================
    # LEVEL 1: BASIC FIELDS
    # =====================
    name = fields.Char(string="Nom complet", required=True)
    email = fields.Char(string="Email")
    telephone = fields.Char(string="Téléphone")
    cin = fields.Char(string="CIN")
    notes = fields.Text(string="Remarques")

    date_inscription = fields.Date(
        string="Date d'inscription",
        default=fields.Date.today
    )

    # =====================
    # LEVEL 2: WORKFLOW
    # =====================
    statut = fields.Selection(
        [
            ('nouveau', 'Nouveau'),
            ('valide', 'Validé'),
            ('annule', 'Annulé'),
        ],
        string="Statut",
        default='nouveau',
        tracking=True
    )

    # =====================
    # LEVEL 1: VALIDATION
    # =====================
    @api.constrains('email')
    def _check_email(self):
        for rec in self:
            if rec.email and '@' not in rec.email:
                raise ValidationError("Adresse email invalide.")

    # =====================
    # LEVEL 2: ACTIONS
    # =====================
    def action_valider(self):
        for rec in self:
            rec.statut = 'valide'

    def action_annuler(self):
        for rec in self:
            rec.statut = 'annule'
