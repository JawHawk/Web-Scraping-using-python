#same way used for my extension Anichinu

from bs4 import BeautifulSoup
import requests
import json
file = open('Trending_anime.json','a')

dic = {"Trending_animes":[]}


URL = 'https://zoro.to/home'
page = requests.get(URL)
soup = BeautifulSoup(page.content,'html.parser')

trending_Animes = soup.find_all('div',class_='swiper-slide item-qtip')
for x in trending_Animes:
    dic['Trending_animes'].append({"name":(x.a).img['title'],"link":'https://zoro.to'+(x.a)['href']})

objk = json.dumps(dic,indent=4)
file.write(objk)