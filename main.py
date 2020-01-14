import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
print(indeed_result.text)

# https://stackoverflow.com/jobs?q=python
