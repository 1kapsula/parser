import bs4
import json

class Parser:
    data_list = None

    def __init__(self, source):
        self.source = source

    def parse(self):
        if self.data_list is None:
            with open(self.source, 'rb') as f:
                self.data_list = []
                soup = bs4.BeautifulSoup(f.read(), 'html.parser')
                articles_soup = soup.find_all('article', attrs={'class': 'uho rubric_lenta__item js-article'})
                for x in articles_soup:
                    one_post = {}
                    one_post['header'] = x.get('data-article-title').replace('\xa0', ' ')
                    one_post['date'] = x.find_next('p', attrs={'uho__tag rubric_lenta__item_tag hide_desktop'}).get_text().strip().replace(" ","")
                    one_post['time to read'] = x.get('data-article-ttr')
                    one_post['comments count'] = x.get('data-article-comments-count')
                    self.data_list.append(one_post)
        return self.data_list

    def save(self, path):
        if path is not None:
            with open(path, 'w') as f:
                f.write(json.dumps(self.data_list, indent=4, ensure_ascii=False))