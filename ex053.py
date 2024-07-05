# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

# Listas.
num = list()
impar = list()
par = list()

#Estrutura de Repetição.
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

#Definindo se é PAR ou IPAR.
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        if v % 2 == 1:
            impar.append(v)

# Apresentando Resultado.
print('=-' * 30)
print(f'A lista completa é {num}')
print(f'Os numeros PARES são: {par} ')
print(f'OS numeros IMPARES são: {impar} ')
print('=-' * 30)

#FIM
