# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Collect data from news website + stored in csv

import csv
from urllib import request
from bs4 import BeautifulSoup

header = ['Title', 'Date', 'Full Content']
data = []
time = ''


url = "http://www.bbc.co.uk/news/election-us-2016-35791008"
html = request.urlopen(url).read().decode('utf8')


soup = BeautifulSoup(html, 'html.parser')
title = soup.find('title')

data += title

time += soup.find('time').text

data += [time]

content = soup.find('div')
article = ''

for x in content.findAll(class_="ssrcss-uf6wea-RichTextComponentWrapper e1xue1i85"):
    article = article + ' ' + x.text

data += [article]

with open("C:/Users/user/OneDrive/Рабочий стол/Scrapper.csv", "w") as scrapper_csv:
    writer = csv.writer(scrapper_csv, lineterminator='\n')
    writer.writerow(header)
    writer.writerow(data)

with open("C:/Users/user/OneDrive/Рабочий стол/Scrapper.txt", "w") as scrapper_word:
    for i in range(len(header)):
        scrapper_word.write(header[i] + ':\t' + data[i])
        scrapper_word.write('\n')
