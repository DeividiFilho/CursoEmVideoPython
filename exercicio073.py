times = ('Corinthians', 'Atlético-MG', 'São Paulo',
 'Botafogo', 'Santos', 'Coritiba', 'Avaí', 'América-MG',
 'Palmeiras', 'Bragantino', 'Internacional', 'Fluminense',
 'Goiás', 'Cuiabá', 'Athletico-PR', 'Flamengo',
 'Juventude',  'Ceará SC', 'Atlético-GO', 'Fortaleza' )

print("-" * 20)
print(f'\nLista de times: {times}\n')
print("-" * 20)
print(f'Os 5 primeiros são {times[0:5]}')
print("-" * 20)
print(f'Os 4 na zoma de rebaixamento {times[-4:]}')
print("-" * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print("-" * 20)
print(f'O Corinthians está na {times.index("Corinthians")+1} posição ')
print("-" * 20)
