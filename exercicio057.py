sexo = str(input(" Informe seu genêro [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
  sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo == 'M' or sexo == 'm':
  print('Sexo Masculino registrado  com sucesso!')
if sexo == 'F' or sexo == 'f':
  print("Sexo feminino registrado com sucesso!")
