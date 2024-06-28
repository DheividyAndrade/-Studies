# TUPLAS.

cont = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 
       'Sete', 'Oito', 'Nove', 'Dez')
while True:
    num = int(input('Digite um Numero entre 0 e 10: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o numero {cont[num]}')
