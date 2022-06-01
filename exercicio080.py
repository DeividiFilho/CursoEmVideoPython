list = []

for c in range(0, 5):
  num = int(input('Digite um valor: '))
  if c == 0:
    list.append(num)
    print('Primeiro valor. Adicionando no final da lista...')

  elif num > list[len(list)-1]:
    list.append(num)

  else:
    pos = 0

    while pos < len(list):
      if num <= list[pos]:
        list.insert(pos, num)
        break
      pos += 1

print("Os valores digitados foram: ", list)