import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/list?titleId=736277&weekday=sun")

soup = BeautifulSoup(res.text,"html.parser")

webtoons = soup.find_all("td",attrs={"class":"title"})
for webtoon in webtoons:
    title = webtoon.a.get_text()
    link = "https://comic.naver.com"+webtoon.a["href"]
    print(title,link)