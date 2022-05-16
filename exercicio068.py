from random import randint
cont = 0

while True:
  pc = randint(0, 10)
  jogador = int(input("Qual número você escolheu? "))
  total = jogador + pc
  impar_par = '  '

  while impar_par not in "PpIi":
    impar_par = str(input("Impar ou par? [P/I] ")).upper().strip()[0]
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

  if impar_par == 'P':
    if total % 2 == 0:
      print(f"\nJogador escolheu {jogador} e o Computador escolheu {pc}. A soma foi {total} e o Jogador \nGANHOU!!!")  
      cont += 1

    else:
      print(f"\nJogador escolheu {jogador} e o Computador escolheu {pc}. A soma foi {total} e o jogador teve {cont} vitórias e o Jogador \nPERDEU!!!")  
      break

  elif impar_par == "I":
    if total % 2 == 1:
      print(f"\nJogador escolheu {jogador} e o Computador escolheu {pc}. A soma foi {total} e o Jogador \nGANHOU!!!")  
      cont += 1

    else:
      print(f"\nJogador escolheu {jogador} e o Computador escolheu {pc}. A soma foi {total} e o jogador teve {cont} vitórias e o Jogador \nPERDEU!!!")  
      break
  

