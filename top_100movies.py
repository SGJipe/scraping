import requests
from bs4 import BeautifulSoup
#import requests_cache

# Do the same with https://stacker.com/stories/1587/100-best-movies-all-time

#equests_cache.install_cache('demo_cache')


class moviesScraper(object):

    def __init__(self, url):
        self. url = url
        self.data = {}

    def get_request(self):
        return requests.get(self.url).text

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')

    def get_top_100_movies(self):
        movies = self.get_soup().find_all('div', {"class": "ct-slideshow__slide__text-container"})
        title = []
        description = {}
        for information in movies[1:5]:
            title.append(information.h2.get_text().replace("\n", ""))
            carac = information.select(class_="ct-slideshow__slide__text-container__description").find_all('p')
            for description in informations:
                print(type(informations))
                print(description.get_text().strip().replace("\n", ""))

        #self.data[]
        #self.data[f'{" ".join(title)}']
        return self.data


if __name__ == "__main__":
    urlToScrape = r'https://stacker.com/stories/1587/100-best-movies-all-time'
    solution = moviesScraper(urlToScrape).get_top_100_movies()
    for title, rating in solution.items():
        print(f"{title}: {rating}")
