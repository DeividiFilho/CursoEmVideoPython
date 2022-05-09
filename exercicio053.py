frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

# inverso = junto[::-1] por fatiamaento

for letra in range(len(junto) -1, -1, -1):
  inverso += junto[letra]
if inverso == junto:
  print(junto, inverso, "\n É Palíndromo!")
else:
  print(junto, inverso, "\n Não é Palíndromo!")