from urllib import request
from flask import Flask, render_template
from bs4 import BeautifulSoup  
import requests 
app=Flask(__name__)

source=requests.get('http://quotes.toscrape.com').text
soup=BeautifulSoup(source, 'lxml')

quote=soup.find('div', class_='quote')
quotetext=quote.span.text
print(quotetext)

author=soup.find('small', class_='author')
authortext=author.text
print(authortext)

app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)