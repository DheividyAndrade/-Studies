# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                    
from time import sleep

def contador(i, f, p):
    # resolvendo o problema da contagem negativa
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=-' * 20)
    print(f'contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)
    

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
        sleep(0.3)

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 20)
print('Agora é a sua vez de personalizar sua contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
