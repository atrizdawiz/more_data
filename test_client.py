import uuid
import os
import json
import urllib.request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from pathlib import Path
class test_client:
    
    def __init__(self):
        self.ad_title = None
        self.ad_description = None
        self.ad_price = None
        self.ad_id = None
        self.ad_type = None
        #self.ad_image_url = ad_image_url    
    def update_test(self):
        filepath = Path("C:/Repos/more_data/test_data/annons.html")
        filtered_ad_html = SoupStrainer('div', {'class': 'section'})
        ad_type = "typeS"
        with open(filepath, 'rb') as html:
            soup = BeautifulSoup(html, 'html.parser', parse_only=filtered_ad_html)

            # Dig down to interesting ad data
            ad_title = soup.h2.contents[0]
            ad_description = soup.find(itemprop="description").text
            ad_price = soup.find(itemprop="price").contents[0]

            # Update fields
            self.ad_title = ad_title
            self.ad_description = ad_description
            self.ad_price = ad_price
            self.ad_id = str(uuid.uuid1())
            self.ad_type = ad_type
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    def some_keyword_hits(self):
        keywords = ["YamAhA"]
        lower_case_keywords = [x.lower() for x in keywords]
        for x in lower_case_keywords:
            if x in self.ad_title.lower().split(" ") or x in self.ad_description.lower().split(" "):
                print("Ad has relevant keywords!")
                return True
            else:
                return False
                
    def shouldBePersisted(self):
        if self.ad_type == "typeS":
            return self.some_keyword_hits()
        else:
            return False