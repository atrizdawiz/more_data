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
#print("Type is: " + str(ad_type))
#print("URL is: " + str(ad_url))

# Fetch, filter and parse HTML from actual ad
ad_html = urllib.request.urlopen(ad_url)
filtered_ad_html = SoupStrainer('div', {'class': 'section'})
parsed_ad = BeautifulSoup(ad_html, 'html.parser', parse_only=filtered_ad_html)

# Dig down to interesting ad data
ad_title = parsed_ad.h2.contents[0]
ad_description = parsed_ad.find(itemprop="description").contents[0]
ad_price = parsed_ad.find(itemprop="price").contents[0]

#ad_html2 = urllib.request.urlopen(ad_url)
#image_html = SoupStrainer('div', {'class': 'showimage'})
#parsed_image_info = BeautifulSoup(ad_html2, 'html.parser', parse_only=image_html)
#ad_image_url = "http://vend.se/"+parsed_image_info.a.img['src']

# Print ad variables
#print("Title: "+ ad_title)
#print("Description: " + ad_description)
#print("Price: " + ad_price)
#print("Image URL: " + ad_image_url)

# filter out ads that do not correspond to my keywords
# add interesting ads to database