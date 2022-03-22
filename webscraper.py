import requests
from bs4 import BeautifulSoup
urls = ["computers/laptops", "computers/tablets", "phones/touch"]
webScraperPage = r'https://webscraper.io/test-sites/e-commerce/allinone'

odProducts = {}

for url in urls:
    pageToScrape = webScraperPage + "/" + url
    #print(pageToScrape)
    pageToScrape = requests.get(pageToScrape)
    pageToScrape = pageToScrape.text

    soup = BeautifulSoup(pageToScrape, 'html.parser')
    row = soup.find_all(attrs={"class": "row"}, limit=3)[2]
    #print(row)
    columns = row.find_all('div')
    #print(columns)
    for datas in columns[0:1]:
        #print(type(datas))
        #print(datas.get_text().strip().replace("\n\n", ",").replace("\n", ""))
        product_title = list(map(lambda data: data.get_text().strip().replace("\n\n", "|").replace("\n", ""), datas))
        #print(type(product_title))
        #product_title = list(datas.get_text().strip())
        #odProducts[f'{" ".join(product_title[0])}'] = save[1][0]
        test = list(product_title)
        print(test)
        print(test[1])
        #print("------")
        #print(len(product_title))
        #print(list(product_title))

