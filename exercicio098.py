from time import sleep

def contador(i, f, p):

  if p < 0:
    p *= -1
  
  if p == 0:
    p = 1

  print(f'\nContagem de {i} até {f} em {p}')
  sleep(1)


  if i < f:
    cont = i

    while cont <= f:
      print(f'{cont}', end=' ', flush=True)
      sleep(0.3)
      cont += p
    print('\nFim')

  else:
    cont = i

    while cont >= f:
      print(f'{cont} ', end=' ', flush=True)
      sleep(0.3)
      cont -= p
    print('\nFim')


ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini, fim, pas)