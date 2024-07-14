# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#IMPORTANDO BIBLIOTECAS
from random import randint
from time import sleep
from operator import itemgetter

#RANDOMIZANDO RESULTADO.
jogo = { 'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
#RANQUEANDO LISTA.
ranking = list()
print('VALORES SORTEADOS: ')
for k, v in jogo.items():
    print(f'{k} tirou o {v} no dado. ')
    sleep(1)
#DEIXANDO O DICIONARIO EM ORGEM.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) 
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for k, v in enumerate(ranking):
    print(f'  {k+1}º lugar: com {v[0]}. ')
    sleep(1)
#FIM
