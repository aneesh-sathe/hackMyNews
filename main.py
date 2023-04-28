from bs4 import BeautifulSoup
import requests as r
import smtplib
import datetime as dt


def sendArticle():
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

    send_name = article_name[index + 1]
    send_link = article_link[index - 1]

    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(PROCESS.ENV.EMAIL, PROCESS.ENV.PASS)
        con.sendmail(
            from_addr=PROCESS.ENV.EMAIL,
            to_addrs=PROCESS.ENV.EMAIL,
            msg=f"Subject: YC Hacker News\n\n{send_name}{send_link}")


while True:
    current_time = dt.datetime.now().time()
    if current_time.hour == 0 and current_time.minute == 0:  # Send Mail at 00:00 Hours
        sendArticle()
