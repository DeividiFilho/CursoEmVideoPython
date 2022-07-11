
def leiaInt(msg):

  ok = False
  valor = 0

  while True:
    try:
      n = str(input(msg))

    except (ValueError, TypeError):
      print('ERRO: Por favor, digite um número válido.')
      continue

    else:
      return n


    if n.isnumeric():
      valor = int(n)
      ok = True
    
    else:
      print('ERRO, digite um número válido!!')
    
    if ok:
      break
  
  return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')