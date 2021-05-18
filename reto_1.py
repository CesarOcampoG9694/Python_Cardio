def area_triangulo(base_1,altura_1):
    area =  (base_1*altura_1) / 2
    return area


def run():
    bienvenida = """
    Bienvenido al reto 1 - Calcularemos el área de un triángulo

    """
    print(bienvenida)
    base = int(input('Ingresa la base del triángulo: '))
    altura = int(input('Ingresa la altura del triángulo: '))

    area_tri = area_triangulo(base,altura)

    print('El área del triangulo es de: ',area_tri)


if __name__ == '__main__':
    run()
    