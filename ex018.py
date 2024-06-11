A = int(input('Digite um numero inteiro: '))
B = int(input('Digite o segundo numero inteiro: '))
if A > B:
    print('{} é maior que {}'.format(A, B))
elif B > A:
    print('{} é maior que {}'.format(B, A))
elif A == B:
    print('Não existe valor maior, os 2 são iguais!')
