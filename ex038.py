# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

from time import sleep
while True:
    n = int(input('Digite um numero: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('finalizado..')
sleep(1)
print('Programa Finalizado. Volte Sempre!')
