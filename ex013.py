salario = float(input('Qual o salario do funcionario? R$:'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario *10 / 100)
print('Quem ganhar R${} passou a ganhar R${} agora'.format(salario, novo))
