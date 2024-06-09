distancia = float(input('Quantos km você pretende viajar? '))
km = distancia * 0.50
print('Você esta preste a começar uma viagem!')
if km < 200:
    print('Vai lhe custar R${:.2f} no valor promocional'.format(km))
else:
    print('Ficou no valor de R${:.2f}'.format(km))
