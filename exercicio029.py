velo = int(input("Qual a velocidade do seu carro em km/h? :"))

if velo < 80 :
  print("Você está em velocidade adequada!\n Boa viagem!")
elif velo == 80 :
  print("Você está no limite. Cuidado!")
elif velo >= 120 :
  print("Você está muito acima da velocidade permitida. Multa gravissíma!\n Pague o valor de R$ 500,00")
else :
  print("Você está acima da velocidade permitida! Multa moderada!\n Pague o valor de R$ 210,00")