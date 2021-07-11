import requests
from bs4 import BeautifulSoup
res = requests.get("https://comic.naver.com/webtoon/weekday")

soup = BeautifulSoup(res.text,"html.parser")


weeks = soup.find("div", attrs ={"class":"list_area daily_all"}).find_all("div", attrs={"class":"col_inner"})
#find_all은 해당 값을 모두 리스트로 받아오므로 요소에 접근하는 get_text가 안되므로 for문을 통해 리스트를 풀어서 접근해야함
for week in weeks:
    print(week.get_text())
#find는 해당값중 맨 처음만 불러오고 요소에 저장하므로 get_text()가 적용됨

