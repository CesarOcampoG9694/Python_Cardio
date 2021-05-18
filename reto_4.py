import math
from typing import cast

def run():
    print('Calcularemos el volúmen de un cilintro')
    radio = int(input('Ingresa el radio del cilintro: '))
    altura = int(input('Ingresa la altura del cilindro: '))
    pi = math.pi

    volumen = pi*math.pow(radio,2)*altura
    
    print('El volúmen de tu cilindro es de: ',round(volumen,2))


if __name__ == '__main__':
    run()