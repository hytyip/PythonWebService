from zeep import Client
from zeep.transports import Transport
from zeep.exceptions import Fault


def Success1_Test():
    # Success test with correct data
    client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')

    try:
        result = client.service.ConvertSpeed(
        '100', 'kilometersPerhour', 'milesPerhour')
        print('Pass Success 1 Test, it return ' + str(result))
        assert result == 62.137, 'Wrong data'
    except Fault as exc:
        print(exc.message)


def ZeroValue_Test():
    # Success test with 0
    client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')

    try:
        result = client.service.ConvertSpeed(
            '0', 'kilometersPerhour', 'milesPerhour')
        print('Pass wrong value test, it return ' + str(result))
        assert result == 0, 'Wrong data'
    except Fault as exc:
        print(exc.message)


def Error1_Test():
    # Error test with incorrect data
    client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')

    try:
        result = client.service.ConvertSpeed( '', 'kilometersPerhour', 'milesPerhour')
    except Fault as exc:
        #print(exc.message)
        assert 'Input string was not in a correct format' in exc.message, 'Wrong error message'
        #print(exc.code)
        #print(exc.detail)
        #print(exc.subcodes)
        print 'Pass the error test 1, it displays correct error'

def Error2_Test():
    # Error test with invalid value
    client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')

    try:
        result = client.service.ConvertSpeed( '100', 'kilometersPerhour', ' ')
    except Fault as exc:
        #print(exc.message)
        assert 'is not a valid value for SpeedUnit' in exc.message, 'Wrong error message'
        #print(exc.code)
        #print(exc.detail)
        #print(exc.subcodes)
        print 'Pass the error test 2, it displays correct error'

#Perform the Tests
Success1_Test()
ZeroValue_Test()
Error1_Test()
Error2_Test()
