from time import sleep

def maior(* num):

  cont = maior = 0
  print('\nAnalisando os valores recebidos...\n')

  for valor in num:
    print(f'{valor} ', end='')
    sleep(0.3)

    if cont == 0:
      maior = valor
    
    else:

      if valor > maior:
        maior = valor
    cont += 1
  
  print(f'\nForam informados {cont} valores ao todo')
  print(f'\nO maior valor informado é {maior} !!')

