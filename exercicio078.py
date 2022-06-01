list = []

for i in range(0, 5):
  n = int(input(f"Digite um valor para a posição {i}: "))
  list += [n]
  
print(list)
print(f'O maior valor digitado foi: ', (max(list)))
print(f'O menor valor digitado foi: ', (min(list)))
