# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:43:54 2026

@author: andre
"""
#%%
##import das bibliotecas
import requests
import xml.etree.ElementTree as et
import re
#%%

#%%
##import docker em XML
endpoint = 'https://divvy-tripdata.s3.amazonaws.com/?list-type=2'
response = requests.get(endpoint)
print(response.text)
#%%

#%%
##transformar em arq virtual
ns = {'s3': 'http://s3.amazonaws.com/doc/2006-03-01/'}
raiz = et.fromstring(response.content) 
elementos_contents = raiz.findall('s3:Contents', ns)
##loop de insercao dos arqs
arquivos_zip = []
for elemento in elementos_contents:
    chave = elemento.find('s3:Key', ns)

    if chave is not None:
        nome_arq = chave.text

        if nome_arq.endswith(".zip"):
            arquivos_zip.append(nome_arq)
print(arquivos_zip)
        
#%%
