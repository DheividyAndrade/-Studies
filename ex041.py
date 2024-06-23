# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('==' * 30)
print('{:-^60}'.format('ATACADÃO DE PREÇOS'))
print('==' * 30)

total =quantM = prodB = 0
barato = ''
while True:
    prod = str(input('Digite o Produto: '))
    valor = float(input('Digite o Valor: '))
    prodB += 1
    if prodB == 1:
        menor = valor
        barato = prod
    else:
        if valor < menor:
            menor = valor
            barato = prod
    total += valor
    if valor >= 1000:
        quantM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^60}'.format('FIM DO PROGRAMA'))
print(f'Total da compra foi: R${total:.2f}')
print(f'O total de produtos que ultrapassam 1000 Reais foram: {quantM}')
print(f'O produto mais barato foi {barato} que custa: R${menor:.2f}')
