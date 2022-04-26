from random import randint

pc = randint(0, 5)
print("---" * 5)
print("Vou pensar em um número")
print("---" * 5)
jogador = int(input("Em que número eu pensei? (entre 0 e 5): "))
print("---" * 5)

if jogador == pc :
  print("PARABÉNS! Você me venceu!")
else:
  print("Você perdeu!! Eu pensei no número {}".format(pc))
