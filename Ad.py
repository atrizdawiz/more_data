import uuid
import os
import json
import urllib.request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
class Ad:
    def __init__(self):
        self.ad_title = None
        self.ad_description = None
        self.ad_price = None
        self.ad_id = None
        self.ad_type = None
        #self.ad_image_url = ad_image_url

    def update(self):
        # Proxy Settings for running it at work
        #proxies = urllib.request.ProxyHandler({"http" : "os.environ['ICA_PROXY']", "https" : "os.environ['ICA_PROXY']"})
        #opener = urllib.request.build_opener(proxies)
        #urllib.request.install_opener(opener)
        
        # HTML Fetch
        page = urllib.request.urlopen('https://vend.se/')
        first_interesting=SoupStrainer('ul', {'class': 'list'})
        soup = BeautifulSoup(page, 'html.parser', parse_only=first_interesting)

        # dig down to interesting data
        ad_type = soup.li.ul.li['class'][0]
        ad_url = 'https://www.vend.se/'+soup.li.ul.li.find_next_sibling('li').a['href']

        # Fetch, filter and parse HTML from actual ad
        ad_html = urllib.request.urlopen(ad_url)
        filtered_ad_html = SoupStrainer('div', {'class': 'section'})
        parsed_ad = BeautifulSoup(ad_html, 'html.parser', parse_only=filtered_ad_html)

        # Dig down to interesting ad data
        ad_title = parsed_ad.h2.contents[0]
        ad_description = parsed_ad.find(itemprop="description").text
        ad_price = parsed_ad.find(itemprop="price").contents[0]

        # Update fields
        self.ad_title = ad_title
        self.ad_description = ad_description
        self.ad_price = ad_price
        self.ad_id = str(uuid.uuid1())
        self.ad_type = ad_type
        print(ad_title + ad_description + ad_price + ad_id + ad_type)
    def interesting_ad(self):
        keywords = ["roland mks-20", "mutron", "yamaha dx7", "Avalon"]
        for x in keywords:
            if x in self.ad_title or x in self.ad_description:
                print("Ad has relevant keywords!")
                return True
            else:
                return False
                
    def shouldBePersisted(self):
        if self.ad_type == "typeS" and self.interesting_ad():
            return True
        # check that ad is not in db already and
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)