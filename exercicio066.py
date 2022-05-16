qntd = soma = 0

while True:  
  n = int(input("Digite um número: "))
  if n == 999:
     break
  soma += n
  qntd += 1

print(f"A quantidade de número digitado foi {qntd} e a soma deles é {soma}")
