time = list()
jogador = dict()
partidas = list()
partidas = list()

while True:
  jogador.clear()
  jogador['nome'] = str(input("Nome do jogador: "))

  total = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))
  partidas.clear()

  for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))

  jogador['gols'] = partidas[:]
  jogador['total'] = sum(partidas)
  time.append(jogador.copy())

  while True:
    resp = str(input("Quer continuar? [S/N] ")).upper()[0]

    if resp in 'SN':
      break
    print('Erro! Responda com S ou N.')

  if resp == 'N':
    break

for i in jogador.keys():
  print(f'{i:<15}', end=' ')
print()

print('--'*25)

for i, j in enumerate(time):
  print(f'{i}', end=' ')

  for d in j.values():
    print(f'{str(d)}', end=' ')
  print()


print('--'*25)

for i, v in enumerate(jogador['gols']):
  print(f' => Na partida {i} fez {v} gols')

#print(f'Foi um total de {jogador["total"]} gols.')