import random
nome1 = input("Qual o primeiro nome ? :")
nome2 = input("Qual o segundo nome ? :")
nome3 = input("Qual o terceiro nome ? :")
nome4 = input("Qual o quarto nome ? :")

lista = [nome1, nome2, nome3, nome4]  
random.shuffle(lista)
print(lista)