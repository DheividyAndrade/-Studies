# Faça um programa que leia nome e peso de várias pessoas:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


# Estrutura de repetição/ Listas.
temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

#MAIOR e MENOR peso Calculo.
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

# Pergunta.
    perg = str(input('Quer continuar? [S/N]'))
    if perg in 'Nn':
        break
print('=-' * 30)
print(f'Foram cadastradas {len(princ)} pessoas. ')
print(f'A quantidade de pessoas com maior peso foi de {mai}KG ')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'A quantidade de pessoas com menor peso foi de {men}KG ')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}')   

#FIM
