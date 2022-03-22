import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('demo_cache')

odBibleReference = {
    'Psaumes': 'PSA'
}

class BibleScraping(object):

    def __init__(self, current_url):
        self.url = current_url
        self.data = {}

    def get_request(self):
        return requests.get(self.url).text

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')

    def get_books_with_reference(self):
        print(self.get_soup())
        books_list = self.get_soup().find(class_="list ma0 pa0 bg-white pb5 min-vh-100")
        print(books_list)


if __name__ == "__main__":
    sBibleUrl = r'https://www.bible.com/fr/bible/152/GEN.1.S21'
    get_bible = BibleScraping(sBibleUrl).get_books_with_reference()
    #livre = input("Choisir son livre : ")
    #chapitre = input("Quelle chapitre ? ")
    #verset = input("Quel verset ? ")
    #print(livre + " " + chapitre + " : " + verset)
    #urlToScrape = r'https://www.bible.com/fr/bible/152/'+BibleReference[livre]+'.'+chapitre+'.S21'
    #print(urlToScrape)