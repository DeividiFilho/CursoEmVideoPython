from random import randint

itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0,2)
jogador = int(input("Suas opções\n[0] Pedra\n[1] Papel\n[2] Tesoura\n Qual sua escolha :"))

print("--" * 20)
print("O computador escolheu {}".format(itens[computador]))
print("O jogador jogou  {}".format(itens[jogador]))
print("--" * 20)

if computador == 0:  #PEDRA
  if jogador == 0:
    print("\nEMPATE")
  elif jogador == 1:
    print("\nJOGADOR VENCEU!")
  else:
    print("\nCOMPUTADOR VENCEU!")

elif computador == 1:  #PAPEL
  if jogador == 0:
    print("\nCOMPUTADOR VENCEU")
  elif jogador == 1:
    print("\nEMPATE")
  else:
    print("\nJOGADOR VENCEU!")
elif computador == 2:  #TESOURA 
  if jogador == 0:
    print("\nJOGADOR VENCEU")
  elif jogador == 1:
    print("\nCOMPUTADOR VENCEU!")
  else:
    print("\nEMPATE")


