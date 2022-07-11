def fatorial(n, show=False):
  ''' -> Calcula o fatorial de um número.
      - N: O número a ser calculado.
      - Show: (Opcional) Mostra a conta ou não.
      - Retur: O valor fatorial de um número n.
  '''

  f = 1
  
  for c in range(n, 0, -1):

    if show:
      print(c, end='')

      if c > 1:
        print(' x ', end='')
      
      else:
        print(' = ', end='')

    f *= c
  
  return f


print(fatorial(5))

help(fatorial)