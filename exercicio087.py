matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = mai = soma_col = 0

for l in range(0, 3):
  for c in range(0, 3):
    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-' * 30)

for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matriz[l][c]:^5}]', end='')
    if matriz[l][c] % 2 == 0:
      soma_par += matriz[l][c]

  print()
print('-' * 30)
print(f'A soma dos valores pares é {soma_par}')

for c in range(0, 3):
  if c == 0:
    mai = matriz[1][c]
  elif matriz[1][c] > mai:
    mai = matriz[1][c]
    
print(f'O maior valor da segunda linha é {mai}.')

for l in range(0, 3):
  soma_col += matriz[l][c]

print(f'A soma dos valores da terceira coluna é: {soma_col}.')
