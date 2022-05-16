print("=="*20)
print("     Bem Vindo ao BANCO CEV!    ")
print("=="*20)

valor = int(input("Qual valor você quer sacar? R$ "))
cedulas = valor//50
resto = valor%50

if cedulas > 0:
    print(f"Total de {cedulas} cédulas de R$50")
cedulas = resto//20
resto %= 20

if cedulas > 0:
    print(f"Total de {cedulas} cédulas de R$20")
cedulas = resto//10
resto %= 10

if cedulas > 0:
    print(f"Total de {cedulas} cédulas de R$10")
cedulas = resto//1

if cedulas > 0:
    print(f"Total de {cedulas} cédulas de R$1")
print("=="*20)
print("    Volte sempre ao BANCO CEV! ")
print("=="*20)