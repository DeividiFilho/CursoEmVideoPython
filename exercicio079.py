numeros = list()

while True:
  num = int(input("Digite um valor: "))

  if num not in numeros:
    numeros.append(num)
    print('Valor adicionado!')
  else:
    print('Valor duplicado. Não foi possível adicionar!')

  r = str(input("Quer continuar? [S/N]: "))
  if r in 'Nn':
    break

numeros.sort()
print(f'Você adicionou os números {numeros}')