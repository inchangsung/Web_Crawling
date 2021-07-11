import requests
from bs4 import BeautifulSoup
res = requests.get("https://comic.naver.com/webtoon/weekday")


res.raise_for_status()
soup = BeautifulSoup(res.text,"html.parser") #문법 해석기

#print(soup.title.get_text())
#print(soup.find("a", attrs={"class":"Nbtn_upload"}))
##class 속성이 Nbun _upload 인 a element를 찾음

#print(soup.find("a"))
##a element를 찾음 (제일 먼저 나온)
#print(soup.find("li", attrs={"class":"rank01"}).find("a").get_text())
rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.next_sibling.next_sibling)

#print(rank1.next_sibling.next_sibling.get_text())
##다음 테그트

    #find_all : 리스트 형태
    #find("a").get_text()
rank2= rank1.find_next_sibling("li")
print(rank2.find("a").get_text())
rank2 = rank2.find_next_sibling("li")

ranks = rank1.find_next_siblings("li")
print(ranks)

print(rank1.a.get_text())
for rank in ranks:
    print(rank.a.get_text())