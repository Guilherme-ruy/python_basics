# -*- coding: utf-8 -*-

print ("Hello World")
print (10 % 3)

x = 15
y = 15

x == y


if x > y:
    print ("X é maior que Y")

elif x == y:
    print ("São iguais")

else:
    print ("Y é maior que X")


teste = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(teste)