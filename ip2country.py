from SOAPpy import WSDL

wsdlFile = 'http://www.w3schools.com/webservices/tempconvert.asmx?WSDL'
server = WSDL.Proxy(wsdlFile)
print server.show_methods()
print server.