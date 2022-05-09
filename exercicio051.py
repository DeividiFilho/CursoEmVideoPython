# Progressão aritmetrica 

primeiro_termo = int(input("Qual o primeio termo: "))
razao = int(input("Qual a razão: "))
decimo_termo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo_termo + razao, razao):
  print(i)