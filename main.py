import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# https://stackoverflow.com/jobs?q=python

pagination = indeed_soup.find("div", {"class": "pagination"})
# list
pages = pagination.find_all('a')

spans = []
for page in pages: 
  spans.append(page.find("span"))
spans = spans[:-1]