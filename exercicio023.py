num = int(input("Digite um número de até 4 dígito : "))
n = str(num)
if num > 9999 :
  print("Digite um número de até 4 dígitos Muggle!")
else :
  print("Analisando o número {}".format(num))
  print("A Unidade é: {}".format(n[3]))
  print("A Dezena é: {}".format(n[2]))
  print("A Centena é: {}".format(n[1]))
  print("A Milher é: {}".format(n[0]))