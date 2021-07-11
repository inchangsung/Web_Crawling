import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/list?titleId=736277&weekday=sun")

soup = BeautifulSoup(res.text,"html.parser")

webtoons = soup.find("table",attrs ={"class":"viewList"}).find_all("td",attrs = {"class":"title"})

for webtoon in webtoons:
    print(webtoon.get_text())