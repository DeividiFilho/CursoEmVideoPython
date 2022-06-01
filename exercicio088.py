from random import randint

lista = list()
jogos = list()
cont = 0

print('-' * 30)
print('\n         MEGA SENA\n')
print('-' * 30)

quant = int(input('Quantos jogos você quer sortear: '))
tot = 1

while tot <= quant:
  cont = 0

  while True:
    num = randint(1, 60)

    if num not in lista:
      lista.append(num)
      cont += 1

    if cont >= 6:
      break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(f'Os números sorteados foram {jogos}')

'''for i in jogos:
  print(f'Jogo {i}: ')'''