def conversor_medida(tipo_conversion,variable_1):
    if tipo_conversion == 1:
        return variable_1 * 1.609344
    else:
        return variable_1 / 1.609344
        

def run():
    mensaje = """
    Bienvenido al conversor de medidas. 
    
    Por favor Elija el tipo de conversión que quiere realizar
    1.- Millas a Kilometros
    2.- Kilometros a Millas
    
    Ingrese una opción: """

    opcion = int(input(mensaje))

    medida = int(input('Ingrese la medida a convertir: '))

    conversion = conversor_medida(opcion,medida)

    print('La conversión de ',medida, ' es de ',conversion)

if __name__ == '__main__':
    run()
    