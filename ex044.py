times = ('Corintians', 'Flamengo', 'São Paulo', 'Palmeiras', 'Fluminense',
          'Vasco', 'Santos', 'Chapecoense', 'Gremio')
print('=-' * 65)
print(f'Lista de Times: {times}')
print('=-' * 65)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('=-' * 65)
print(f'Os 4 Ultimos colocados são: {times[-4:]}')
print('=-' * 65)
print(f'Os times em ordem ALFABETICAS: {sorted(times)}')
print('=-' * 65)
print(f'O time da Chapecoense esta na  {times.index('Chapecoense')+1}ª')
