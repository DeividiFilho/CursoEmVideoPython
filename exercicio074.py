from random import randint

n = (randint(0,50), randint(0,50), randint(0,50),
 randint(0,50), randint(0,50))

max = max(n)
min = min(n) 

print(f'\nO computador sorteou os valores: {n}')
print(f'\nO maior valor sorteado foi {max} e o menor foi {min}')