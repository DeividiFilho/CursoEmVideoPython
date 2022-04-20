preco = float(input("Qual é o valor do produto? R$"))
desconto = float(input("Qual é o desconto? % :"))

novo = preco - (preco * desconto / 100)

print("O produto que custava R$", preco , "agora ésta custando", novo )