# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Qual seu sexo: [M/F] ')).strip().upper()[0]
print(sexo)
while sexo not in 'MmfF':
    sexo = str(input('Dados invalidos! por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
