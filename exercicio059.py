n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0

while opcao != 5:
  print('''  \n  [ 1 ] somar
  [ 2 ] multiplicar
  [ 3 ] maior
  [ 4 ] novos números 
  [ 5 ] sair do programa''')
  opcao = int(input("\nQual é a sua opção? "))
  if opcao == 1:
    print(" \nO resultado da soma de", n1, "+", n2, "é :", n1+n2)
  elif opcao == 2:
    print("\nO resultado da mutiplicação de", n1, "*", n2, "é:", n1*n2)
  elif opcao == 3:
    if n1 > n2:
      print("\nO maior número entre", n1, "e", n2, "é: ", n1)
    elif n2 > n1:
      print("\nO maior número entre", n1, "e", n2, "é: ", n2)
    else :
      print("Os números são iguais.")
  elif opcao == 4:
    n1 = int(input("\nDigite um novo número: "))
    n2 = int(input("\nDigite um segundo novo número: "))
  elif opcao == 5:
    print("\nPrograma finalizando... ")
  else:
    print("\nDigite uma opção disponível! ")
print("\nVocê encerrou o programa. Obrigado e volte sempre!")