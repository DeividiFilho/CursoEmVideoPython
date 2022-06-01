num = (int(input('Digite o primeiro número: ')),
 int(input('Digite o segundo número: ')),
 int(input('Digite o terceiro número: ')),
 int(input('Digite o quarto número: ')))

print(f'Você digitou os valores {num}')
print(f'\nO número 9 aparecceu {num.count(9)} vezes')

if 3 in num:
  print(f'\nO número 3 apareceu na {num.index(3)+1}° posição')
else:
  print('\nO valor 3 não foi digitado!')
  
print(f'\nOs valores pares foram', end=' ')
for i in num:
  if i % 2 == 0:
    print(i, end=' ')