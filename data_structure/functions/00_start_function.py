def hello_world():
    print('Hello World')
hello_world()

def bom_dia_nome(nome):
    print(f'Bom dia {nome}')
bom_dia_nome(nome='Gui')


def calcular_total(numeros):
    print(type(sum(numeros)))
    return type(sum(numeros))


print(calcular_total([10, 15, 30]))

n1 = int(input('n1 = '))
n2 = int(input('n2 = '))


print(calcular_total(f'{n1}{n2}'))