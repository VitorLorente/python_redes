#usr/bin/venv_pyredes Python3
#Programação de Redes com Python

import requests

def geocode(address):
	parameters = {'address': address, 'sensor': 'false'}
	base = 'http://maps.googleapis.com/maps/api/geocode/json'
	response = requests.get(base, params=parameters)
	answer = response.json()
	print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
	geocode('Julio Sayago, 405, São Paulo, SP')
