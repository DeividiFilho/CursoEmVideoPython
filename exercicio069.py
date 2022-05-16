print("Seja Bem-Vindo ao programa de cadastro!\n")
homem = adulto = girl = 0


while True:
  nome = str(input("Seu nome: ")).lower().strip()
  idade = int(input("Sua idade: "))
  sexo = str(input("Seu sexo [M/F]: ")).lower().strip()

  parar = str(input("\nQuer continuar a cadastrar? [S/N]: ")).lower().strip()

  if parar == 'n':
    parar = str(input("Quer continuar a cadastrar? [S/N]: ")).lower().strip()

    break
  
  if idade > 18:
    adulto += 1
  
  if sexo == "m":
    homem += 1

  if girl < 20 and sexo == "f":
    girl += 1

print(f"No total tem {idade} maiores de 18 anos. \nTem {homem} cadastrado. \nE tem {girl} mulhres com menos de 20 anos cadastrado.")
