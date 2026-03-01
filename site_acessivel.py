import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://google.com')
except urllib.error.URLError:
    print('Erro ao acessar o site')
else:
    print('Site acessível com sucesso!')
