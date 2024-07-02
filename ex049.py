# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

#Lendo 5 valores 
valores = []
mai = 0 
men = 0 
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
# calculo para identificar MAIOR e MENOR.

    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]

print('=-' * 20)
print(f'Os valores foram {valores}')    
print(f'O MAIOR valor digitado é {mai} nas posições ', end='')
# posição do MAIOR valor.
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()
# osição do MENOR valor.
print(f'O MENOR valor digitado é {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()
print('=-' * 20)

#fim