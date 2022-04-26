salario = float(input("Qual o seu salário? :"))

if salario <= 1250:
  print("Você terá um aumento de 15%.\nO salário reajustado será de :", salario + (salario * 0.15))
else :
  print("Você terá um aumento de 10%.\nO salário final será de :", salario + (salario * 0.1))