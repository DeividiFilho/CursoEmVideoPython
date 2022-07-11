
def voto(ano):
  from datetime import date

  atual = date.today().year
  idade = atual - ano 

  if idade < 16:
    return f'\nCom {idade} anos: Não Vota!'

  elif 16 <= idade < 18 or idade >= 65:
    return f'\nCom {idade} anos: O voto é opcional!'

  else:
    return f'\nCom {idade} anos: O voto é obrigatório!'

nasc = int(input('Qual seu ano de nascimento: '))
print(voto(nasc))