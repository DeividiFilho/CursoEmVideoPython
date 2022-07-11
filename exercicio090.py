aluno = dict()
aluno['Nome'] = str(input("Nome: "))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
  aluno['situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
  aluno['situação'] = 'Recuperação'
else:
  aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
  print(f'\n{k} é igual a {v}')