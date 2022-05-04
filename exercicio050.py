s = 0
c = 0
for i in range(1, 7):
  n = int(input("Digite  o {} valor : ".format(i) ))
  if n % 2 == 0:
    s += n
    c += 1
print("O total de números pares informado foi :", c)
print("A soma dos números pares é:", s)

