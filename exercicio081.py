list = []

while True:
  list.append(int(input('Digite um valor: ')))
  resp = str(input('Quer continuar? [S/N] '))

  if resp in 'Nn':
    break
print(f'\nA quantidade de valores digitados é: {len(list)} elementos ')

list.sort(reverse=True)
print(f'\nOs valores em ordem descrescentes são {list}')

if 5 in list:
  print('\nO número 5 faz parte da lista!')
else:
  print('\nO número 5 não faz parte da lista!')
