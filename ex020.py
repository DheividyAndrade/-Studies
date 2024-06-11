n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
soma = (n1 + n2) / 2
if soma < 5.0:
    print('REPROVADO! sua média é de {:.1f}'.format(soma))
elif soma < 6.9:
    print('RECUPERAÇÃO! sua média é de {:.1f}'.format(soma))
elif soma >= 7.0:
    print('APROVADO! sua media é de {:.1f}'.format(soma))
    