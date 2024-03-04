teste = 'teste'
memory = 160000

print(teste is memory)

print(teste is not memory)

print('-------------------')

if teste is not memory:
    print('Não ocupam a mesma região de memoria')
else:
    print('Ocupa a mesma região de memoria')

