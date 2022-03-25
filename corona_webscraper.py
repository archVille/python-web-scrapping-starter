# from urllib import request
# from flask import Flask, render_template
from bs4 import BeautifulSoup  
import requests 
# app=Flask(__name__)

url = 'https://www.worldometers.info/coronavirus/'
req = requests.get(url).text
str = BeautifulSoup(req, "html.parser")

data = str.find_all('div', class_="maincounter-number")

print(data[0].text)
print()
