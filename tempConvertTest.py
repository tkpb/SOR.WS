from suds.client import Client

wsdlFile = 'http://www.w3schools.com/webservices/tempconvert.asmx?WSDL'
client = Client(wsdlFile)
userImput = ''
tempChoice = 0


def fromC(temperature):
    return client.service.CelsiusToFahrenheit(temperature)


def fromF(temperature):
    return client.service.FahrenheitToCelsius(temperature)


def setup():
    global tempChoice
    valid = False
    while not valid:
        tempChoice = input("Escolha a operacao: (1) C para F (2) F para C\n")
        if tempChoice == 1:
            valid = True
        elif tempChoice == 2:
            valid = True


setup()
while len(userImput) > 0:
    userImput = input("Temperatura para converter: ")
    if tempChoice == 1:
        print 'Result: ' + fromC(userImput) + 'F'
    elif tempChoice == 2:
        print 'Result: ' + fromF(userImput) + 'C'
    else:
        setup()