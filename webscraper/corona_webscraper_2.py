# from urllib import request
from flask import Flask, render_template
from bs4 import BeautifulSoup  
import requests 
app=Flask(__name__)

url = 'https://www.worldometers.info/coronavirus/'
req = requests.get(url)
str = BeautifulSoup(req.text, "html.parser")

data = str.find_all("div", class_="maincounter-number")
# print(data)

data = data[0]


app.route('/')
def home():
    return render_template('index2.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)