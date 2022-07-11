
jogador = dict()
partidas = list()
jogador['nome'] = str(input("Nome do jogador: "))
total = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))

for c in range(0, total):
  partidas.append(int(input(f'Quantos gols na partida {c}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('--'*25)
print(jogador)

print('--'*25)
for k, v in jogador.items():
  print(f'\nO campo {k} tem o valor {v}')

print('--'*25)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas. ')
for i, v in enumerate(jogador['gols']):
  print(f' => Na partida {i} fez {v} gols')

print(f'Foi um total de {jogador["total"]} gols.')