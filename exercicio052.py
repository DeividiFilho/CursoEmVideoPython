n = int(input("Digite um número inteiro: "))
tot = 0

for i in range(1, n+1):
  if n % i == 00:
    print('\033[34m')
    tot += 1
  else:
    print('\033[m')
  print(i, end=" ")
print("\n\033[mO número", n, "foi divisível", tot, "vezez")
if tot == 2:
  print("O número", n, "é PRIMO!")
elif n == 1:
  print("O número 1 NÃO É PRIMO!")
else:
  print("O número", n, "NÃO É PRIMO!")