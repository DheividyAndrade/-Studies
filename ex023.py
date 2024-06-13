print('{:=^40})'.format('LOJAS ANDRADE'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em R${:.2f} SEM JURSO'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcel = int(input('Quantas parcelas você deseja? '))
    parcela = total / totalparcel
    print('Sua compra sera parcelada em {}x R${:.2F} COM JUROS'.format(totalparcel, parcela))
else:
    total= 0
    print('OPÇÃO INVALIDA! tente novamente. ')
print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(preço, total))
