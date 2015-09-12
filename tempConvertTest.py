from suds.client import Client

wsdlFile = 'http://www.w3schools.com/webservices/tempconvert.asmx?WSDL'

client = Client(wsdlFile)
tF = '212'
tC = '0'
print '%s F = %s C\n' % (tF, client.service.FahrenheitToCelsius(tF))
print '%s C = %s F' % (tC, client.service.CelsiusToFahrenheit(tC))