n1 = float(input("Digite a sua nota: "))
n2 = float(input("Digite a sua nota: "))

media = (n1 + n2) / 2

print("A sua média é:", media)
if media > 6:
  print("Você passou.\nFoi APROVADO. \nAprovete suas férias!")
elif media < 4:
  print("Você foi REPROVADO.\nRefaça o semestre!")
else:
  print("Você está de recuperação.\nFaça a prova e boa sorte! :)")
