from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O angulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cose = cos(radians(ângulo))
print('O angulo de {} tem o coseno de {:.2f}'.format(ângulo, cose))
tang = tan(radians(ângulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(ângulo, tang))
