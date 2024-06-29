num = (int(input('Digite um numero: ')), 
       int(input('Digite um numero: ')), 
        int(input('Digite um numero: ')), 
        int(input('Digite um numero: ')))
print(f'Você digitou os valores {num} ')
print(f'O numero 9 apareceu {num.count(9)}x')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª possição ')
else:
    print(f'O valor 3 não foi Digitado em nenhuma posição. ')
print(f'Os numeros pares foram ', end= '')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
