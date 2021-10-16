#Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Accessing websites
url = input('Enter URL: ')
position = int(input('Enter position: '))
count = int(input('Enter count: '))

url_list = list()

#Retrieve all of the anchor tags
for i in range(count - 1):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag_list = list()
    for tag in tags:
        y = tag.get('href', None)
        tag_list.append(y)

    url = taglist[pos]
    url_list.append(url)

print()
