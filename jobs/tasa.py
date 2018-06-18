#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------
# Copyright:   (c) Cesar Herdenez 2018
# Licence:     Apache License Version 2.0
# ---------------------------------------------

from requests import get
from bs4 import BeautifulSoup as bs4
from lxml import html

URL = 'https://dolar.wilkinsonpc.com.co/'
TASA = 'tasas-de-interes/'

# Tasa de usura
'''
// TODO:
 * cronjob para revisar la tasa los 2 ultimos dias del mes y 2 primeros
   dias del mes
 * reducir el xpath
'''
response = get('{}{}{}'.format(URL, TASA, 'tasa-usura-consumo-ordinario.html'))
tree = html.fromstring(response.content)
tasa = tree.xpath(
    '/html/body/div[3]/div[5]/div[1]/div/div/div[2]/div/div/div[2]/span[2]/text()')
# Tasa de usura
print(float(tasa[0]))
# Tasa de usura desde BS4

data = bs4(response.text, 'html.parser')
tasa = data.findAll('span', {"class": 'numero'})
print(tasa[0].text)
# IBR

response = get('{}{}'.format(URL, 'ibr.html'))
data = bs4(response.text, 'html.parser')
tasa = data.findAll('span', {"class": 'indicador_numero'})
# Tasa IBR
'''
la tasa IBR del dia es la 1
'''
d = tasa[0].text
d = d.replace(' ', '').replace('%', '')
print(float(d))
