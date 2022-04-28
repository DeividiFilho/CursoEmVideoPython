ano_nascimento = int(input("Qual é o seu ano de nascimento? :"))
idade =  2022 - ano_nascimento

print("\nSua idade é :", idade)

if idade <= 9:
  print("\nSua categoria é MIRIM")
elif idade <= 14 > 9:
  print("\nSua categoria é INFANTIL")
elif idade <= 19 > 14:
  print("\nSua categoria é JUNIOR")
elif idade <= 25 > 19:
  print("\nSua categoria é SÊNIOR")
elif idade > 25:
  print("\nSua categoria é MASTER")