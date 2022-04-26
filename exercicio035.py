a = int(input("Qual o primeiro segmento: "))
b = int(input("Qual o segundo segmento: "))
c = int(input("Qual o terceiro segmento: "))

if a < b+c and b < a+c and c < a+b:
  print("Os segmentos acimas PODEM formar triângulo!!")
else:
  print("Os segmentos acima NÃO PODEM formar triângulos!")  