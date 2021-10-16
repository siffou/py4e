from urllib import request
import xml.etree.ElementTree as ET

url = input('Enter url: ')
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')

icount = len(results)
isum = 0

for result in results:
    isum += int(result.find('count').text)
print(icount)
print(isum)
