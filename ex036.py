# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quantidade = media = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma + num
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma / quantidade
print('Você digitou {} numeros e a media foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
