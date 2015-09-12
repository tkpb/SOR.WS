from suds.client import Client

wsdlFile = 'http://www.w3schools.com/webservices/tempconvert.asmx?WSDL'
client = Client(wsdlFile)


def fromC(temperature):
    return client.service.CelsiusToFahrenheit(temperature)


def fromF(temperature):
    return client.service.FahrenheitToCelsius(temperature)