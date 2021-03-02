"""Case-study #4 Парсинг web-страниц
Разработчики:
Турчинович М., Зубарева Т., Костылев М.
"""
import urllib.request
url = 'https://www.nfl.com/players/bryce-petty/stats/'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("nfl-c-player-header__title")
name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
print(name)
total = text.find ('TOTAL')
end_str = text.find('</tfoot>', total)
str = text[total : end_str]
str = str.replace('</th>', ' ')
print (str)