import requests
from bs4 import BeautifulSoup
#import requests_cache

# Do the same with https://stacker.com/stories/1587/100-best-movies-all-time

#equests_cache.install_cache('demo_cache')


class PokemonScraper(object):

    def __init__(self, url):
        self.url = url
        self.data = []

    def get_request(self):
        return requests.get(self.url).text

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')

    def get_first_150_pokemon(self):
        pokemon = self.get_soup().find(class_="hlist-separated").find_all('a')
        return list(map(lambda pokemon: pokemon.get_text(), pokemon))

    def get_pokemon_base_stats(self):
        table = self.get_soup().find_all('table', class_="vitals-table")
        table_body = table.tbody
        for rows in table_body('tr'):
            if(len(rows))
        print(base_stat)


if __name__ == "__main__":
    urlToScrape = r'https://en.wikipedia.org/wiki/List_of_generation_I_Pok%C3%A9mon'
    solution = PokemonScraper(urlToScrape).get_first_150_pokemon()
    for nameEN in solution[:1]:
        #print(f"{nameEN}")
        urlToScrape2 = r'https://pokemondb.net/pokedex/' + nameEN
        print(urlToScrape2)
        #urlToScrape2 = r'https://pokemondb.net/pokedex/' + nameEN
        stats = PokemonScraper(urlToScrape2).get_pokemon_base_stats()
