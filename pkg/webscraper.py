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
        self.url_wg = "https://www.wg-gesucht.de/wohnungen-in-Berlin.8.2.1.0.html?offer_filter=1&city_id=8&noDeact=1&dFr=1598911200&categories%5B%5D=2&rent_types%5B%5D=0&rMax=1200&rmMin=2&rmMax=3&exc=2"
        self.url_ebay = "https://www.ebay-kleinanzeigen.de/s-auf-zeit-wg/entire_accommodation/berlin/zwischenmiete/k0c199l3331+auf_zeit_wg.art_s:entire_accommodation"
        self.web = webbot.Browser()
        self.web.go_to(self.url_wg)
        self.delay = 3
        time.sleep(self.delay)
        self.document_links = []
       # self.web.type("Göttingen - 37073", into='Suche')


    def find_links(self):

        self.data = []

        self.html_page = self.web.get_page_source()
        time.sleep(self.delay)

        soup = BeautifulSoup(self.html_page, features="html.parser")
        time.sleep(self.delay)
        time.sleep(self.delay)
        time.sleep(self.delay)


        for link in soup.findAll('a', attrs={'href': re.compile("^wohnungen")}):
            self.document_links.append("https://www.wg-gesucht.de/" + link.get('href'))

        return self.document_links

    def find_links_ebay(self):

        time.sleep(self.delay)
        self.web.go_to(self.url_ebay)

        self.html_page = self.web.get_page_source()
        time.sleep(self.delay)

        soup = BeautifulSoup(self.html_page, features="html.parser")
        time.sleep(self.delay)
        time.sleep(self.delay)
        time.sleep(self.delay)

        for link in soup.findAll('a', attrs={'href': re.compile("^/s-anzeige")}):
            self.document_links.append("https://www.ebay-kleinanzeigen.de/" + link.get('href'))

        return self.document_links




if __name__ == "__main__":
    ws = WebScraper()


    list = ws.find_links_ebay()


