listagem = ('Lapis', 9.50, 
            'Borracha', 5.00, 
            'Caderno', 30.00, 
            'Tesoura', 3.30, 
            'Mochila', 60.00)
print('-' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5}')
print('-' * 40)
