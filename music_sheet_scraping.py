import requests
import requests_cache
import time
from bs4 import BeautifulSoup

requests_cache.install_cache("demo_cache")

class MusicSheetScraping(object):

    def __init__(self, url):
        self.base_url = "https://www.flutetunes.com"
        self.url = url
        self.music_urls = []
        self.data = {}

    def get_request(self):
        return requests.get(self.url).text

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')

    def get_music_item_list(self, limit):
        table = self.get_soup().table
        rows = table.find_all('tr')
        for row in rows[1:limit+1]:
            get_url = row.find('a').get('href')
            self.music_urls.append(self.base_url + get_url)
        return self.music_urls


    def get_sheet_music_information(self):
        table = self.get_soup().table
        rows = table.find_all('tr')
        for row in rows:
            save = []
            get_tds = row.select('th + td')
            get_ths = row.find('th')

            if not get_ths is None:
                get_ths = get_ths.get_text()
                save.append(get_ths)

            for td in get_tds:
                get_link = td.find('a')
                if not get_link is None:
                    get_href = get_link.get('href')
                    td_info = self.base_url + get_href
                else:
                    td_info = td.get_text()
                save.append(td_info)

                self.data[save[0]] = save[1]
        return(self.data)

if __name__ == "__main__":
    timeItTakes = time.time()
    letter = input('Choose a letter : ')
    number_of_musics = int(input('Choose a number of wanting music : '))

    urlFirstTime = r'https://www.flutetunes.com/titles.php?a='+letter
    music_list_items = MusicSheetScraping(urlFirstTime).get_music_item_list(number_of_musics)
    for music_item in music_list_items:
        print(music_item)
        music_sheet = MusicSheetScraping(music_item).get_sheet_music_information()
        print(music_sheet)
    endtime = time.time() - timeItTakes
    print(endtime)
