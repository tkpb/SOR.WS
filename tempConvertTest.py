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
        tempChoice = input("Escolha a operacao: (1) C para F (2) F para C")
        if tempChoice == 1:
            valid = True
        elif tempChoice == 2:
            valid = True


setup()
while userImput != 'exit':
    userImput = input("Temperatura para converter: ")
    if tempChoice == 1:
        fromC(userImput)
    elif tempChoice == 2:
        fromF(userImput)
    else:
        setup()