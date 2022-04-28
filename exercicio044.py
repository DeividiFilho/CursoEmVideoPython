preco = float(input("Qual o valor da compra? R$: "))
pagamento = int(input("Qual a forma de pagamento?\n[1] DINHEIRO \n[2] À VISTA CARTÃO \n[3] 2x NO CARTÃO \n[4] 3x OU MAIS NO CARTÃO\n"))

if pagamento == 1:
  print("\nÀ vista em dinheiro, seu pagamento será de R$:", (preco - (preco * 0.1)))
elif pagamento == 2:
  print("\nÀ vista no cartão seu pagamento será de R$:", (preco - (preco * 0.05)))
elif pagamento == 3:
  print("\nEm até 2x no cartão o valor total será de R$:", preco)
elif pagamento == 4:
  print("\nEm 3x ou mais o valor total será de R$:", (preco + (preco * 0.2)))
else :
  print("\nInforme uma forma de pagamento válida!!")
