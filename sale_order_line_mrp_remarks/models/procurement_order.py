# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api


class ProcurementOrder(models.Model):
    _inherit = 'procurement.order'

    def _prepare_mo_vals(self, bom):
        res = super(ProcurementOrder, self)._prepare_mo_vals(bom)
        remarks_list = []
        if self.group_id:
            for procurement in self.group_id.procurement_ids:
                if procurement.sale_line_id and \
                        procurement.sale_line_id.remarks:
                    remarks_list.append(procurement.sale_line_id.remarks)
        res['remarks'] = ','.join(remarks_list)
        return res
