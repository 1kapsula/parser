import requests
import datetime

class Downloader:
    html_page = None
    def __init__(self, url, params, method='GET'):
        self.url = url
        self.url += "/".join([f"{str(x[1])}" for x in params.items()])
        print(self.url)
        self.params = params
        self.method = method

    def get_html(self):
        req = requests.get(self.url, self.params)
        if req.status_code == 200:
            req = req.content
            self.html_page = req
            return self.html_page
        else:
            raise ValueError(f"Не удалось выполнить запрос. Код ошибки {req.status_code}")

    def save(self, path):
        with open(path, 'wb') as f:
            f.write(self.html_page)