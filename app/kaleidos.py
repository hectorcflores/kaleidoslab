from lxml import html
import requests
import string
import omdb
import json
import operator

import re

#cineteca website
flik_site = "http://www.cinetecanacional.net/controlador.php?opcion=carteleraDia"
page = requests.get(flik_site)
tree = html.fromstring(page.text)

#only titles in Cartelera del Dia
# titles_delDia = tree.xpath('//p[@class="peliculaTitulo"]/text()')
#all titles in Cartelera
titles_enCartelera = tree.xpath('//*[@id="principalContainer"]/div[6]/div/ul[2]/li/a/text()')
film_data = tree.xpath('//p[@class="peliculaMiniFicha"]/text()')



#create dictionary of flicks for cartelera del dia
#if odmb request is True
#you can also get tomatoMeter and tomatoUserMeter
imdbRating_dict = {}
fliks_runtime= []
fliks_info = []
titles_notFound = []
for i in range(len(titles_enCartelera)):
	try:
		res = omdb.request(t=titles_enCartelera[i], r='json', tomatoes=True)
		json_content = res.content
		content = json.loads(json_content)
		#print json.dumps(content, indent=2)
		if (content['Response']== "True" and content['imdbRating'] != 'N/A'):
			fliks_runtime.append([content['Title'], content['Runtime']])
			fliks_info.append([content['imdbRating'], content['Title'], content['Director'],
			content['Country'], content['Year'], content['Runtime']])
			imdbRating_dict[content['Title']] = content['imdbRating']
			#tomatoMeter_dict[content['Title']] = content['tomatoMeter']
			#tomatoUserMeter_dict[content['Title']] = content['tomatoUserMeter']
		else:
			titles_notFound.append(titles_enCartelera[i])
			continue
	except:
		continue

#sort fliks_info by idmbRating
sorted_fliks_info = sorted(fliks_info, key=operator.itemgetter(0), reverse=True)

fliks = [["86%", "Asteroide", "Marcelo Tobar", "Mexico", 2015, "96 mins." ],
["57%", "Violencia", "Marcelo Tobar", "Estados Unidos", 2014, "87 mins."], 
["78%", "La tribu", "Marcelo Tobar",  "Argentina", 2014, "108 mins."]]

films=sorted_fliks_info