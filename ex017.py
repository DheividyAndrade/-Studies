num = int(input('Digite um numero inteiro: '))
print('''escolha uma das base como conversão: 
      [ 1 ] converter para BINARIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido em BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido em OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida! tente novamente.')
