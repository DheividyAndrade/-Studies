from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador 'pensar'
print('\033[0:43m-=-\033[m' * 20)
print('Vou pensar entre um numero entre 0 e 5. tente adivinhar...')
print('\033[0:43m-=-\033[m' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador tenta "adivinhar"
print('\033[0:31mPROCESSANDO...')
sleep(2)
if jogador == computador:
    print('\033[0:32mPARABÉNS! você conseguiu me vencer! ')
else:
    print('\033[0:31mGANHEI! eu pensei no numero {} e não no {} '.format(computador, jogador))
