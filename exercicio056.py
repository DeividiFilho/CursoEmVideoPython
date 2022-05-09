media = 0
maior_homem = 0
nome_velho = 0
mulher20 = 0

for i in range(1, 5):
  print("------- {}° PESSOA -------\n".format(i))
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [M/F]: ')).strip().upper()
  media += idade
  if i == 1 and sexo == "M":
    maior_homem = idade
    nome_velho = nome
  if sexo == "M" and idade > maior_homem:
    maior_homem = idade
    nome_velho = nome
  if sexo == 'F' and idade < 20:
    mulher20 += 1

media_idade = media / 4
print("A média de idade do grupo é: ", media_idade, "anos")
print("O homem mais velho tem", maior_homem, "anos e seu nome é ", nome_velho)
print("Ao todo são ", mulher20, "mulheres com menos de 20 anos!")
