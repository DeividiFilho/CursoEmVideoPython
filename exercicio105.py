def notas(* n, sit=False):
  ''' 
  -> Função para analisar notas de alunos.

  - Para n: Uma ou masis notas dos alunos (Aceita vários valores inteiros)
  - Para sit: Valor opcional, indicando a situação em que os alunos se encontra.
  - Para len, max, min, sum/len: São as funções de python onde é possivel saber quantos números foi digitado, o maior número, o menoor número e a média (soma de todos os números e divisão pela quantidade números adicionado).
  = Para return: Dicionário que retorna várias informação sobre as notas.

  '''

  r = dict()
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['média'] = sum(n)/len(n)

  if sit:

    if r['média'] >= 7:
      r['situação'] = 'Boa'
    
    elif r['média'] >= 5:
      r['situação'] = 'Razoável'

    else:
      r['situação'] = 'Ruim'


  return r



resp = notas(5.5, 2.5, 9, 8.5, 10, sit=True)

print(resp)
help(notas)