username = input('Digite seu nome: ')
username_size = len(username)


if username.isalpha():
    if username_size >= 1:
        if username_size <= 4:
            print('Seu nome é de tamanho curto')

        elif username_size >= 5 and username_size <= 6:
            print ('Seu nome é de tamanho normal')

        else:
            print ('Seu nome é de tamanho grande')
    
    else:
        print('Nome inválido')
else:
    print('Digite apenas letras do alfabeto')