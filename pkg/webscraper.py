import re
import webbot
import time
import pickle
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


class WebScraper:
    """
    WebScraper
    """

    def __init__(self):
        self.url = "https://www.wg-gesucht.de/wohnungen-in-Berlin.8.2.1.0.html?offer_filter=1&city_id=8&noDeact=1&dFr=1598911200&categories%5B%5D=2&rent_types%5B%5D=0&rMax=1200&rmMin=2&rmMax=3&exc=2"
        self.web = webbot.Browser()
        self.web.go_to(self.url)
        self.delay = 3
        time.sleep(self.delay)
       # self.web.type("Göttingen - 37073", into='Suche')


    def find_links(self):
        document_links = []
        self.data = []

        self.html_page = self.web.get_page_source()
        time.sleep(self.delay)

        soup = BeautifulSoup(self.html_page, features="html.parser")
        time.sleep(self.delay)
        time.sleep(self.delay)
        time.sleep(self.delay)


        for link in soup.findAll('a', attrs={'href': re.compile("^wohnungen")}):
            document_links.append("https://www.wg-gesucht.de/" + link.get('href'))

        return document_links


if __name__ == "__main__":
    ws = WebScraper()


    list = ws.find_links()


