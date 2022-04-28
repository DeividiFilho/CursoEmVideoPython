
n1 = int(input("O primeiro segmento: "))
n2 = int(input("O segundo segmento: "))
n3 = int(input("O terceiro segmento: "))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
  print("\nOs segmentos acima PODEM formar triângulo!")
  if n1 == n2 == n3:
    print("\nÉ um triângulo Equilátero!")
  elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
    print("\nÉ unm triângulo Isóceles!")
  elif n1 != n2 != n3:
    print("\nÉ um triângulo Escaleno!")
else:
  print("\nOs segmentos acima NÃO PODEM formar triângulos!")

