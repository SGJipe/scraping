import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('demo_cache')


class SiteScraper(object):

    def __init__(self, current_url):
        self.url = current_url
        self.data = {}

    def make_request(self):
        return requests.get(self.url).text

    def make_soup(self):
        return BeautifulSoup(self.make_request(), 'html.parser')

    def get_links(self):
        soup = self.make_soup()
        return soup.find_all(class_='ct-slideshow__slide__text-container')

    def get_data(self):
        raw_data = self.get_links()
        for data_point in raw_data[1:]:
            title = data_point.h2.get_text().replace('\n', '')
            carac = data_point.select('div.ct-slideshow__slide__text-container__description')
            description = data_point.select('p:last-of-type')
            for element in carac:
                self.data[title] = element.p.get_text().split('\n')
            for element in description:
                self.data[title].append(element.get_text())
        return self.data

if __name__ == "__main__":
    get_links = SiteScraper(r'https://stacker.com/stories/1587/100-best-movies-all-time').get_data()
    for key, value in get_links.items():
        print(key, value)