from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from pyngrok import ngrok

#Calculadora con la suma y resta.
class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(ctx, a, b):
        return a - b

application = Application([CalculatorService],
                          tns='calculator',  # Target Namespace
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    server = make_server('localhost', 8000, wsgi_app)

    public_url = ngrok.connect(addr="8000")
    print("Public URL:", public_url)

    server.serve_forever()
