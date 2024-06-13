peso = float(input('Digite seu peso: (kg)'))
altura = float(input('Digite sua altura: (m)'))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('você esta com PESO IDEAL!')
elif 25 <= imc < 30:
    print('você esta com SOBREPESO!')
elif 30 <= imc < 40:
    print('cuidado! OBESIDADE!')
elif imc >= 40:
    print('ALERTA! OBESIDADE MÓRBIDA!!')
