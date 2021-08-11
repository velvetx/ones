from bs4 import BeautifulSoup


class DataParser:
    def __init__(self):
        self.result = []

    def get_html_parser(self, list_with_results):
        for html in list_with_results:
            soup = BeautifulSoup(html, 'lxml')
            line = soup.find_all('a', 'list-info__title')
            for name in line:
                self.result.append(self.filtering_names(name.text))
        return self.result

    @staticmethod
    def filtering_names(name):
        return name.replace(' ', ' ')