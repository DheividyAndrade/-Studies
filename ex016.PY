# O programa a seguir vai perguntar, o valor da casa, o valor do salário 
# e em quantos anos posso financiar. 

casa = float(input('Valor da casa: R$'))
salário = float(input('Valor do salario: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de {:.2f} Reais em {:.2f} anos, a prestação sera de {:.2f}'.format(casa, anos, prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO! ')
else:
    print('Emprestimo NEGADO!')
