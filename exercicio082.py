list_com = []
list_par = []
list_impar = []

while True:
  num = int(input("Digite um número: "))
  list_com.append(num)
  resp = str(input("Quer continuar? [S/N] "))

  if resp in 'Nn':
    break
  
for i in list_com:
  if i % 2 == 0:
    list_par.append(i)

  elif i % 2 == 1:
    list_impar.append(i)
  
print(f'\nA lista completa é {list_com}')
print(f'A lista de pares é {list_par}')
print(f'A lista de ímpares é {list_impar}')
