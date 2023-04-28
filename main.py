from bs4 import BeautifulSoup
import requests as r
import smtplib
import datetime

res = (r.get("https://news.ycombinator.com/news")).text
soup = BeautifulSoup(res, "html.parser")
article_name = []
article_link = []
article_rating = []
x = soup.find_all(name="span", class_="titleline")
for span in x:
    links = span.find_all("a")
    for link in links:
        article_link.append(link["href"])
        article_name.append(link.getText())

x = soup.find_all(name="span", class_="score")
for votes in x:
    v = votes.getText().split()[0]
    article_rating.append(int(v))


n = len(article_link)

names = article_name[0:n:2]
links = article_link[0:n:2]


print(article_name)
print(names)
