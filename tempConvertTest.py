from suds.client import Client

wsdlFile = 'http://www.w3schools.com/webservices/tempconvert.asmx?WSDL'
#serv_url = 'http://www.w3schools.com/webservices/tempconvert.asmx'

client = Client(wsdlFile)
#print client
tF = '212'
tC = '0'
print '%s F = %s C\n' % (tF, client.service.FahrenheitToCelsius(tF))
print '%s C = %s F' % (tC, client.service.CelsiusToFahrenheit(tC))