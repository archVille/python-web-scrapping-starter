# from urllib import request
# from flask import Flask, render_template
from bs4 import BeautifulSoup  
import requests 
# app=Flask(__name__)

url = 'https://en.wikipedia.org/wiki/2022_in_film'
req = requests.get(url)
str = BeautifulSoup(req.text, "html.parser")

data = str.find_all('table', class_="wikitable")

table_data = []
trs = str.select('table tr')

for tr in trs[1:15]:
    row=[]
    for t in tr.select('td')[:2]:
        row.extend([t.text.strip()])
    table_data.append(row)
data=table_data
    
print(data[0])

print()
