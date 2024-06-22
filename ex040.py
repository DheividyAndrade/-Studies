# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

tot18 = totM = totF =  0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F] ')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            totM += 1
        if sexo == 'F' and idade < 20:
            totF += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas maior de 18 anos: {tot18}')
print(f'Ao todo temos {totM} de homens cadastrados')
print(f'Total de mulheres menores de 20 anos: {totF}')
