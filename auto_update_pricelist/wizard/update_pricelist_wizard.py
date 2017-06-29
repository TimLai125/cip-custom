# -*- coding: utf-8 -*-

from odoo import fields, models, api


class UpdatePricelisrWizard(models.TransientModel):
    _name = "update.pricelist.wizard"

    is_confirm = fields.Boolean(
        string="Confirm?",
    )

    @api.multi
    def action_update_pricelist(self):
        if not self.is_confirm:
            return True
        partners = self.env['res.partner'].sudo().search([('customer','=', True)])
        partners.reset_partner_pricelist()
        return True