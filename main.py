import requests
import requests_cache
import time
from bs4 import BeautifulSoup

requests_cache.install_cache("demo_cache")

class ListOfLOLChampionsScraping(object):

    def __init__(self, url):
        self.url = url
        self.data_list = []
        self.data_dict = {}

    def get_request(self):
        return requests.get(self.url).text

    def get_soup(self):
        return BeautifulSoup(self.get_request(), 'html.parser')

    def get_page_title(self):
        title = self.get_soup().find(class_='page-header__title-wrapper').get_text()
        return title

    def get_page_h2(self, id):
        title = self.get_soup().find(attrs={"id": id}).get_text()
        return title + '\n'

    def get_introduction_text(self):
        text = self.get_soup().find(class_='mw-parser-output').find('p').get_text().replace('. ', '. \n')
        return text

    def get_menu(self):
        ulParent = self.get_soup().select('.toc > ul')
        for li in ulParent:
            text = li.get_text().strip().replace('\n\n\n', '\n').replace('\n\n', '\n')
        return text

    def get_champions_legend(self):
        table = self.get_soup().find(class_='champions-list-legend')
        text = "List of Available Champions"
        rows = table.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            save = []
            for column in columns:
                save.append(column.get_text().replace('\n', ''))
            self.data_dict[save[0]] = save[1]
        return self.data_dict

    def get_table_champions(self):
        table = self.get_soup().find(class_="article-table")
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')

        for row in rows:
            columns = row.find_all('td')
            save = []
            for column in columns:
                cell_data = column.get_text().replace('\n', '')
                save.append(cell_data)

            if len(save) > 1:
                self.data_list.append(save)
        return self.data_list

    def get_upcoming_reduction(self):
        title = self.get_soup().select(" table.article-table + h3")[0]
        reduction_list = title.find_next("ul")
        title = title.get_text()
        test = []
        for reduction in reduction_list:
            if len(reduction.get_text()) > 1:
                test.append(reduction.get_text().strip().replace('\n', ''))
        return title + '\n' + '\n'.join(test)

    def get_list_scrapped_champions(self):
        table = self.get_soup().find(class_='columntemplate').find('ul')
        rows = table.find_all('li')
        for row in rows:
            get_li = row.get_text()
            link = row.find('img').get('data-src')
            self.data_dict[get_li] = link
        return self.data_dict

    def get_trivia(self):
        table = self.get_soup().find(attrs={'id': 'Trivia'}).find_parent().find_next_sibling()
        rows = table.find_all('li')
        rows = table.find_all('li')
        for row in rows[:2]:
            get_li = row.get_text()
            link = row.find('img').get('data-src')
            self.data_dict[get_li] = link
        return self.data_dict

    def get_reference_table(self):
        table = self.get_soup().find(class_='navbox')
        rows = table.find_all('tr')
        for row in rows:
            save = []
            get_tds = row.select('th + td')
            get_ths = row.find('th')

            if not get_ths is None:
                get_ths = get_ths.get_text()
                save.append(get_ths)

            for td in get_tds:
                get_link = td.find_all('a')
                if not get_link is None:
                    td_infos = []
                    for link_href in get_link:
                        get_href = link_href.get('href')
                        td_infos.append(self.url + get_href)
                else:
                    td_info = td.get_text()
                if len(td_infos) > 0:
                    save.append(td_infos)
                else:
                    save.append(td_info)

                self.data_dict[save[0]] = save[1]
        return (self.data_dict)

def get_end_of_paragraph(bool):
    if bool:
        return '\n \n'
    else:
        return '\n'

if __name__ == "__main__":
    timeItTakes = time.time()

    urlToScrape = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
    endOfParagraph = get_end_of_paragraph(True)
    endOfSemiParagraph = get_end_of_paragraph(False)

    title = ListOfLOLChampionsScraping(urlToScrape).get_page_title()
    print(title)

    texte = ListOfLOLChampionsScraping(urlToScrape).get_introduction_text()
    print(texte)

    menu = ListOfLOLChampionsScraping(urlToScrape).get_menu()
    print(menu)

    h2 = ListOfLOLChampionsScraping(urlToScrape).get_page_h2("List_of_Available_Champions")
    print(h2)

    legend = ListOfLOLChampionsScraping(urlToScrape).get_champions_legend()
    print(legend)

    champions = ListOfLOLChampionsScraping(urlToScrape).get_table_champions()
    #print(champions)
    for champion in champions:
        print(champion)

    print(endOfSemiParagraph)

    reduction = ListOfLOLChampionsScraping(urlToScrape).get_upcoming_reduction()
    print(reduction)

    print(endOfParagraph)

    h2 = ListOfLOLChampionsScraping(urlToScrape).get_page_h2("List_of_Scrapped_Champions")
    print(h2)

    scrappedChampions = ListOfLOLChampionsScraping(urlToScrape).get_list_scrapped_champions()
    print(scrappedChampions)

    print(endOfParagraph)

    h2 = ListOfLOLChampionsScraping(urlToScrape).get_page_h2("Trivia")
    print(h2)

    trivia = ListOfLOLChampionsScraping(urlToScrape).get_trivia()
    print(trivia)

    print(endOfParagraph)

    h2 = ListOfLOLChampionsScraping(urlToScrape).get_page_h2("References")
    print(h2)

    reference = ListOfLOLChampionsScraping(urlToScrape).get_reference_table()
    print(reference)

    print(endOfParagraph)

    endtime = time.time() - timeItTakes
    print(endtime)