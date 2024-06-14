#FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA, 
# PARA O ESTOURO DE FOGOS DE ARTIFICIO, INDO DE 10 ATÉ 0, 
# COM UMA PAUSA DE 1 SEGUNDO ENTRE ELAS.

from time import sleep
print('CONTAGEM REGRESSIVA EM!...')
sleep(1)
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BUM!, BUM!, POWWWW!!')
