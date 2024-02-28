#Saldo do Usuário
saldo = 580
saque = input(f"Saldo disponível:{saldo}, Quanto deseja sacar? : ")

try:
    if saque.isdigit() and saque.isnumeric() and int(saque) <= saldo:
        print(f"Valor solicitado:{saque}R$, Saque realizado com sucesso! Seu novo saldo é {int(saldo) - int(saque)}R$")

    else:
        print(f"Valor solicitado:{saque}R$, Saque não realizado! Digitou algo errado ou valor acima do saldo.")
except:
    print("Error")

