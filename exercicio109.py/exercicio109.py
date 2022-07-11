import moeda

p = float(input('Digite o preço: R$: '))

print(f'\nA metade de R${moeda.moeda(p)} é de R${moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é de R${moeda.dobro(p, True)}')
print(f'Aumentando 10% do preço, temos R${moeda.aumentar(p, 10, True)}')
print(f'Com desconto de 30%, temos R${moeda.diminuir(p, 30,True)}')
