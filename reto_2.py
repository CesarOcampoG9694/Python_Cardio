def juego_ppt(tiro_1,tiro_2):
    if (tiro_1 == 'piedra' and tiro_2 == 'tijeras') or (tiro_1 == 'papel' and tiro_2 == 'piedra') or (tiro_1 == 'tijeras' and tiro_2 == 'papel'):
        return 1
    elif (tiro_2 == 'piedra' and tiro_1 == 'tijeras') or ( tiro_2 == 'papel' and tiro_1 == 'piedra') or (tiro_2 == 'tijeras' and tiro_1 == 'papel'):
        return 0
    else:
        return 2

def conv_tiro(tiro):
    if tiro == 1:
        return 'piedra'
    elif tiro == 2:
        return 'papel'
    else:
        return 'tijeras'
    

def run():
    bienvenida = """
    Hoy jugaremos piedra, papel o tijeras, bienvenidos!
    """
    print(bienvenida)

    jugador_1 = input('Ingresa el nombre del jugador 1: ')
    jugador_2 = input('ingrese el nombre del jugador 2: ')
    contador_1 = 0
    contador_2 = 0
    intentos = 1
    print("""Están listos?, comenzamos!, 
    Ten en cuenta que:
    1) Piedra
    2) Papel
    3) Tijeras
    """)

    while intentos <= 3 :
        print('Intento',intentos,': \n')
        tiro_1 = int(input('Ingresa tu tiro ' + jugador_1 +': '))
        tiro_2 = int(input('Ingresa tu tiro ' + jugador_2 + ': '))
        ganador = juego_ppt(conv_tiro(tiro_1),conv_tiro(tiro_2))
        if ganador == 1: #Si gana el jugador 1 te devuelve la función un 1
            contador_1 += 1
        elif ganador == 0: #Si gana el jugador 2 te devuelve la función un 0
            contador_2 += 1
        else:
            print('Nadie gana en este intento')
        intentos += 1
        

    if contador_1 > contador_2:
        print('Felicidades ' + jugador_1 + ' eres el ganador!')
    elif contador_2 > contador_1:
        print('Felicidades ' + jugador_2 + ' eres el ganador!')
    else:
        print('Hubo un empate')
        
if __name__ == '__main__':
    run()