import urllib.request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen('https://vend.se/')

# only parse first ad in new ads
first_interesting=SoupStrainer('ul', {'class': 'list'})
soup = BeautifulSoup(page, 'html.parser', parse_only=first_interesting)

# dig down to interesting data
ad_type = soup.li.ul.li['class'][0]
ad_url = 'https://www.vend.se/'+soup.li.ul.li.find_next_sibling('li').a['href']

# print the acquired data
print("Type is: " + str(ad_type))
print("URL is: " + str(ad_url))
