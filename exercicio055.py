list = []
for i in range(1, 6):
  peso = float(input("Qual o peso da {}° pessoa: ".format(i)))
  list += [peso]
print("\nO maior peso lido foi : ", max(list))
print("O menor peso lido foi: ", min(list))