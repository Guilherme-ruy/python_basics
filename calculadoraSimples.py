while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite o outro número: ')
    op = input('Escolha o operador [+], [-], [/], [*]: ')

    nvalido = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        nvalidos = True
    except:
        nvalido = None

        if nvalido is None:
            print('Valor inválido')
            continue

    op_permitidos = ['+', '-', '/', '*']

    if op not in op_permitidos:
        print ('Operador selecionado inválido')
        continue

    if len(op) > 1:
        print('Apenas um operador por vez amigo')
        continue

    print('Estou realizando a conta :) a minute later')
    contador = 0
    while contador < 3:
        contador += 1
        print('.')

    if op == '+':
        print (f'{n1_float} + {n2_float} = ', n1_float + n2_float)
    elif op == '-':
        print (f'{n1_float} - {n2_float} = ', n1_float - n2_float)
    elif op == '*':
        print (f'{n1_float} * {n2_float} = ', n1_float * n2_float)
    elif op == '/':
        print (f'{n1_float} / {n2_float} = ', n1_float / n2_float)
    else:
        print('Não deveria chegar até aqui rs :D')

    sair = input('Fechar = [F]: ')
    sair = sair.lower()
    if sair == 'f':
        print ('Você saiu')
        break