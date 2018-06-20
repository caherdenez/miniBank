#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------
# Copyright:   (c) Cesar Herdenez 2018
# Licence:     Apache License Version 2.0
# ---------------------------------------------

from requests import get
from bs4 import BeautifulSoup as bs4

URL = 'https://dolar.wilkinsonpc.com.co/'

response = get(URL)
data = bs4(response.content,'html.parser')
tables = data.findAll('table',{'id':'tabla-indicadores_ind_todos'})


# get all row in the table
def get_table_info(table):
    for row in table.findAll('tr'):
        try:
            name = row.find('a').text.replace('ó','o')
            value = row.find('span').text # .replace('$','').replace(',','')
            print('{} ({})'.format(name,value))
        except AttributeError:
            # TODO: Validar el Error
            continue
# # Tasa de usura

# // TODO:
#  - cronjob para revisar la tasa los 2 ultimos dias del mes y 2 primeros dias del mes
response = get('{}{}{}'.format(URL, 'tasas-de-interes/', 'tasa-usura-consumo-ordinario.html'))
data = bs4(response.text, 'html.parser')
tasa = data.findAll('span', {"class": 'numero'})
print(tasa[0].text)
# IBR

response = get('{}{}'.format(URL, 'ibr.html'))
data = bs4(response.text, 'html.parser')
tasa = data.findAll('span', {"class": 'indicador_numero'})
# Tasa IBR
# la tasa IBR del dia es la 1

d = tasa[0].text
d = d.replace(' ', '').replace('%', '')
print(float(d))

## Divisas
cont = 0
for table in tables:
    print(cont)
    get_table_info(table)
    cont += 1
