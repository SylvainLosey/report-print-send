# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 Camptocamp (<http://www.camptocamp.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    printer_input_tray_id = fields.Many2one(
        comodel_name='printing.tray.input',
        string='Default Printer Paper Source',
        domain="[('printer_id', '=', printing_printer_id)]",
        oldname="printer_tray_id"
    )
    printer_output_tray_id = fields.Many2one(
        comodel_name='printing.tray.output',
        string='Default Printer Output Bin',
        domain="[('printer_id', '=', printing_printer_id)]",
    )

    @api.onchange('printing_printer_id')
    def onchange_printing_printer_id(self):
        """ Reset the tray when the printer is changed """
        self.printer_output_tray_id = False
        self.printer_input_tray_id = False
