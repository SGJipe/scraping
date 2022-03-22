import requests
import requests_cache
import time
from bs4 import BeautifulSoup

requests_cache.install_cache("demo_cache")

class FormsScraping(object):

    def __init__(self, url):
        self.url = url
        self.data = []

    def get_request(self):
        return requests.get(self.url).text

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')

    def get_forms_rows_in_list(self):
        rows = self.get_soup().find_all('tr', {'class': 'team'})
        for row in rows:
            columns_information = row.find_all('td')
            save = []
            for information in columns_information:
                get_information = information.get_text()
                if len(get_information) < 2:
                    save.append("empty")
                else:
                    save.append(get_information.strip())

            self.data.append(save)
        return(self.data)

if __name__ == "__main__":
    page_number = 25
    timeItTakes = time.time()
    for i in range(1, page_number):
        urlToScrape = r'http://www.scrapethissite.com/pages/forms/?page_num='+ str(i) +''
        form_lists = FormsScraping(urlToScrape).get_forms_rows_in_list()

        for information_list in form_lists:
            print(information_list)

    endtime = time.time() - timeItTakes
    print(endtime)
