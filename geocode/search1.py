#!usr/bin/venv_pyredes python3
#Programação de Redes com Python

from pygeocoder import Geocoder

if __name__ == '__main__':
	address = 'Rua Julio Sayago, 405, São Paulo, SP'
	print(Geocoder.geocode(address)[0].coordinates)

