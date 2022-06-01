palavras = ('aprender', 'programar', 'linguagem', 'python',
             'curso', 'gratis', 'estudar', 'praticar',
             'trabalhar', 'mercado', 'programador', 'futuro')

for i in palavras:
  print(f'\nNa palavra {i.upper()} temos ', end='')
  for letras in i:
    if letras.lower() in 'aeiou':
      print(letras, end=' ')
    