
#Nome e Idade solicitadas
nome = input("Digite seu nome: ")
idade = input('Digite sua idade: ')

if nome and idade:
 
 #Retorno da variável do nome
 print(f'Seu nome é {nome}')

 #Retorno da variável do nome + [::-1] para inversão
 print(f'Seu nome INVERTIDO é {nome[::-1]}')

 #Retorno do número de caracteres da variável nome com função len
 print(f'O número de caracteres do nome é {len(nome)}')

  #Seu nome contém espaços? Com IF
 if ' ' in nome:
  print('Seu nome contém espaços')

 else:
  print('Seu nome NÃO contém espaços')

 #Primeira letra do seu nome
 print(f'Primeira letra do seu nome é {nome[0]}')
 
 #Última letra do seu nome
 print(f'Última letra do seu nome é {nome[-1]}')

else:
 print('Certifique-se de digitar algo em ambos campos')