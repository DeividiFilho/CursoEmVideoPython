from operator import truediv
from random import randint

computador = randint(0, 10)
print("Sou seu computador... acabei de pensar em um número entrre 0 e 10. \nSerá que consegue advinhar? ")
acertou = False
palpites = 0
 
while not acertou:
  jogador = int(input('Qual seu palpite? '))
  palpites += 1
  if jogador == computador:
    acertou = True
print("ACERTOU com", palpites, "tentativas. PARABÉNS!")