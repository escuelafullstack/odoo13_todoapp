from odoo import models,api
from datetime import datetime

class ReportDetalleMovimiento(models.AbstractModel):
    _name = "report.saldo_app.report_detalle_movimiento"

    @api.model
    def _get_report_values(self,docids,data=None):
        docs = self.env["sa.movimiento"].browse(docids)
        docargs= {
            "docs":docs,
            "fecha": datetime.now().strftime("%m-%d-%Y")
        }

        return docargs