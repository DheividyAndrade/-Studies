# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção. No final, mostre a lista ordenada na tela.


#Criando a lista e a estrutura de repetição.
numeros = list()
for c in range(0, 5):
    numeros.append(int(input(f'Digite o {c} valor: ')))

#Mostrando valores.
print('=-' * 30)
print(f'O valores em ordem são: {sorted(numeros)} ')
print('=-' * 30)

#fim
