from random import randint
from time import sleep


def sorteio(lista):
  print('\nSorteando cinco números, aguarde!\n')

  for cont in range(0, 5):
    n = randint(1, 10)
    lista.append(n)
    print(f'{n} ', end='', flush=True)
    sleep(0.1)
  print('PRONTO')
      

def somaPar(lista):

  soma = 0

  for valor in lista:

    if valor % 2 == 0:
        soma += valor
    
  print(f'\nSomando os valores pares de {lista}\nTemos : {soma}')


numero = list()

sorteio(numero)

somaPar(numero)

