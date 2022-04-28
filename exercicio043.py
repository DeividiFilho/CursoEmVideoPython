peso = float(input("Qual é o seu peso? (kg) "))
altura = float(input("Qual é a sua altura? (m) "))

imc = peso / (altura ** 2)
print("\nSua massa corporal é de :", imc)
if imc < 18.5:
  print("\nVocê está abaixo do peso!")
elif imc >= 18.5 and imc < 25.2:
  print("\nVocê está no peso ideal!")
elif imc >= 25.5 and imc < 30:
  print("\nVocê está com sobrepeso!")
elif imc >= 30 and imc < 40:
  print("\nVocê está obeso!")
else:
  print("Você está com obesidade mórbida!\nCuidado!!")