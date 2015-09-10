from suds.client import Client

wsdlFile = 'http://9kgames.com/WS/WSIP2Country.asmx?WSDL'

client = Client(wsdlFile)
print client