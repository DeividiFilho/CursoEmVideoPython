num = int(input("Escolha um número inteiro: "))
base = input("Qual base você quer converter?\n1 para binário\n2 para octal\n3 para hexadecimal : ")

if base == 1:
  print("convertido para binário é igual a {}".format(num, bin(num)))
elif base == 2:
  print(num, "\nconvertido para octal é :", oct(num))
elif base ==3:
  print(num, "\nconvertido para hexadecimal é :", hex(num))
#else:
  print("Digite uma base válida!")
 
 #base != 1 or base != 2 or base != 3:

