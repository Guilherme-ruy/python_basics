start = input('Digite um valor inteiro: ')

if start.isdigit():
    start= int(start)
    par_ou_impar = start % 2 == 0
    par_ou_impar_texto = 'ímpar'

    if par_ou_impar:
        par_ou_impar_texto = 'par'
        
    print(f'Valor digitado:{start}, ele é {par_ou_impar_texto}')

else:
    print('Você digitou algo diferente de inteiro!')