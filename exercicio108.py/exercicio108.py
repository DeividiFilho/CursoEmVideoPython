import moeda

p = float(input('Digite o preço: R$: '))

print(f'\nA metade de R${moeda.moeda(p)} é de R${moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é de R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% do preço, temos R${moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Com desconto de 30%, temos R${moeda.moeda(moeda.diminuir(p, 30))}')