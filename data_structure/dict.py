nomes = {
    'Guilherme':{'idade': 18},
    'Joamir':{'idade': 48},
    'Lerme':{'idade': 19},
}
print(nomes)
print(nomes['Guilherme'])

#print(nomes['Joamir'[::-1]])
#result: KeyError: 'rimaoJ'

contacts = {
    '123@gmail.com': {'nome': 'João'},
    '2fa@gmail.com': {'nome': 'João'},
    'ccc@gmail.com': {'nome': 'João'},
    'azx@gmail.com': {'nome': 'João'},
    '432@gmail.com': {'nome': 'João'}
}

contacts_2 = contacts.copy()

print(f'seus contatos atuais:{contacts}')


contacts.clear()
print(f'seus contatos atuais após o clear:{contacts}')

print(f'seus contatos para backup:{contacts_2}')

print(id(contacts)) #
print(id(contacts_2)) #

print(contacts_2.values()) #[{'nome': 'João'}, {'nome': 'João'}, {'nome': 'João'}, {'nome': 'João'}, {'nome': 'João'}])