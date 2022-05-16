print("Seja Bem-Vindo ao programa\n")

valor_total = mil_reais = menor_preco = cont = 0
barato = ''

while True:
  nome = str(input("Nome do produto: "))
  preco = float(input("Preço do produto em R$: "))
  valor_total += preco
  cont += 1

  if preco > 1000:
    mil_reais += 1

  if cont == 1:
    menor_preco = preco
  else:
    if preco < menor_preco:
      menor_preco = preco
      barato = nome

  continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
  while continuar not in 'SN':
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

  if continuar == 'N':
    break

print(" FIM DO PROGRAMA")
print(f"\nO valor total é R$: {valor_total}")
print(f"\nO total de proutos que custaram acima de mil reais é de : {mil_reais}")
print(f"\nO produto mais barato é {barato} e custa R$ {menor_preco}")
  