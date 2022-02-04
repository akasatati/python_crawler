import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

load_url = "https://www.fujiya-avic.co.jp/shop/goods/search.aspx?sort=5&genre=A-HDP&category=40&search=x&stock=1"
dummy_user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
html = requests.get(load_url, headers={"User-Agent": dummy_user_agent})

soup = BeautifulSoup(html.content, "html.parser")

lists = []
itemNames = soup.find_all("div", {"class": "block-thumbnail-t--goods-name"})
for itemName in itemNames:
    lists.append(itemName.get_text().strip())

for name in lists:
    print(name)