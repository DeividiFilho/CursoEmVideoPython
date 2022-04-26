dist = float(input("Qual a distância que você vai percorrer? :"))

if dist >= 200:
  print("A sua passagem vai custar {} reais".format(dist * 0.5))
else :
  print("A sua passagem vai custar {} reais".format(dist * 0.45))