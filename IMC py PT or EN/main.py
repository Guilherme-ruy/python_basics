lang = input('Português = PT or English = EN: ').strip().upper()

if lang == 'PT':
  altura = float(input('Digite sua altura, em centímetros: '))
  peso = float(input('Digite seu peso, em quilogramas: '))

  imc = peso / (altura / 100)**2

  print('Considere sua massa muscular :D')
  print(f'Seu IMC {imc:.2f} está classificado como', end=' ')

  if imc < 18.5:
    print('abaixo do peso')
  elif imc <= 24.9:
    print('ok')
  elif imc <= 29.9:
    print('sobrepeso!')
  elif imc <= 34.9:
    print('obesidade grau I')
  elif imc <= 39.9:
    print('obesidade grau II')
  else:
    print('obesidade grau III')

elif lang == 'EN':
  height = float(input('Enter your height, in centimeters: '))
  weight = float(input('Enter your weight, in kilograms: '))

  imc = weight / (height / 100)**2

  print('Consider your muscle mass :D')
  print(f'Your BMI {imc:.2f} is classified as', end=' ')

  if imc < 18.5:
    print('underweight')
  elif imc <= 24.9:
    print('ok')
  elif imc <= 29.9:
    print('overweight!')
  elif imc <= 34.9:
    print('obesity level I')
  elif imc <= 39.9:
    print('obesity level II')
  else:
    print('obesity level III')

else:
  print('PT or EN ?')
