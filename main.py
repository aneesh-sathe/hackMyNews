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
for i in x:
    article_name.append(i.getText())


x = soup.select(selector="span a", class_="titleline")
for content in x:
    if "https:" in content["href"]:
        article_link.append(content["href"])

x = soup.find_all(name="span", class_="score")
for votes in x:
    v = votes.getText().split()[0]
    article_rating.append(int(v))


article_link.pop()  # Removing Footer Links
article_link.pop()
article_link.pop()

max_votes = max(article_rating)
index = article_rating.index(max_votes)

print(article_name[index + 1])
print(article_link[index - 1])
