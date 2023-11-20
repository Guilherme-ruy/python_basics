start = input('Digite a hora atual, sem os minutos!')

try:
    hora = int(start)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print(' Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    elif hora == 24:
        print('24 horas ou meia noite? (0h), digite 0')
    else:
        'Hora desconhecida :d'

except:
    print('Confira a hora digitada :o')