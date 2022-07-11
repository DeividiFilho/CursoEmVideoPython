import urllib
import urllib.request

try:
  site = urllib.request.urlopen('https://www.pudim.com.br')

except urllib.error.URLError: 
  print('\nO site Pudim está indisponível nesse momento!')

else:
  print('\nO site Pudim está acessível nesse momento!')
  print(site.read())