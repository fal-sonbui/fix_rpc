import xmlrpc.client
from odoo.http import Controller, dispatch_rpc, request
from odoo.odoo.addons.base.controller.rpc import RPC

class RPC(Controller):
    def _xmlrpc(self, service):
        """Common method to handle an XML-RPC request."""
        data = request.httprequest.get_data()
        params, method = xmlrpc.client.loads(data)
        result = dispatch_rpc(service, method, params)
        return xmlrpc.client.dumps((result,), methodresponse=1, allow_none=True)
