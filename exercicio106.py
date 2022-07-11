from time import sleep


def ajuda(com):

  titulo(f' Acessando o manual do comando {com} ')
  help(com)
  sleep(0.5)

def titulo(msg, cor=0):

  tam = len(msg) + 5
  print('-' * tam)
  print(f'  {msg}')
  print('-' * tam)
  sleep(1)

  

comando = ''

while True:
  titulo('Sistema de ajuda PyHelp')
  comando = str(input("Função ou Biblioteca : "))

  if comando.upper() == 'FIM':
    break

  else:
    ajuda(comando)

titulo('Até logo!')