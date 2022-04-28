valor_casa = float(input("Qual é o valor da casa? R$: "))
salario = float(input("Qual é seu salário? R$: "))
ano_casa = float(input("Em quantos anos você vai pagar a casa? : "))
prestacao = valor_casa / (ano_casa * 12 )
minimo = salario * 0.3 

if prestacao <= minimo:
  print("Empréstimo APROVADO!")
  print("Para pagar uma casa de R$", valor_casa , "\nA prestação será de :", prestacao ,"Reais", "\nEm", ano_casa,"anos")
else:
  print("Empréstimo NEGADO")
