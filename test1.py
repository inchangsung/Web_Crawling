import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&l=%EB%A7%88%EC%9E%A5%EB%8F%99").text

indeed_soup = BeautifulSoup(indeed_result, "html.parser")

print(type(indeed_result))