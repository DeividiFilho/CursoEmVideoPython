cont = ('zero', 'um', 'dois', 'tres', 'quatro',
 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
  'onze', 'doze', 'treze', 'catorze', 'quinze',
  'dezesseis', 'dezesete', 'dezoito', 'deznove',
  'vinte' )

while True:
  num = int(input("Digite um número entre 0 e 20: "))
  if 0 <= num <= 20:
    break
  print("Você digitou um número errado. Tente novamente")
print(f"Você digitou o número {cont[num]}")
