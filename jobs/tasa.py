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
print(tasa)

# IBR

response = get('{}{}'.format(URL, 'ibr.html'))
tree = html.fromstring(response.content)
# f = tree.xpath('//span[@class="indicador_numero"]')
tasa = tree.xpath()
# Tasa IBR
print(tasa)
