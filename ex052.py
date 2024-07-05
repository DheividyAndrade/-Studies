# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# Estrutura de Repetição.
valores = list()
while True:
    valores.append(int(input('Digite um numero: ')))
    n = str(input('Quer continuar? [S/N]')).upper()
    if n in 'Nn':
        break

# Resultado das questões A,B,C.
print('=-' * 30)
valores.sort(reverse=True)
print(f'Os numeros digitados foram {valores}')
if 5 in valores:
    print(f'O valor 5 está na lista')
else:
    print(f'O valor 5 não está na lista.')
print(f'Foram digitados {len(valores)} numeros ')
print('=-' * 30)

# Fim
