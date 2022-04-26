frase = str(input("Digite uma frase: ")).lower().strip()

print("A letra A aparece {} vezes na frase.".format(frase.count("a")))
print("A primeira letra A aparareceu na posição {}".format(frase.find("a")+1))
print("A ultima letra A aparareceu na posição {}".format(frase.rfind("a")+1))

