import urllib
from BeautifulSoup import *
import re
'''
Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Reno.html 
Find the link at
 position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: L
'''
url = raw_input('Enter URL - ')
position = int(raw_input('Position - '))
deep = int(raw_input('Count - '))
if len(url) < 1: url = 'http://python-data.dr-chuck.net/known_by_Reno.html'

def getUrl(url): #Go to HREF-link and find a lot of other HREF
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    return tags
tags = getUrl(url) #Return a lot of HREF

def hrefBack(position): #Take 'tags' and find URL with 'position' value
    count = 0
    for tag in tags:
        tag = str(tag.get('href', None))
        count += 1
        if count == position:
            return tag
urls = hrefBack(position)

print 'Retrieving:', hrefBack(position)
deeps = 0
while deeps < deep -1:
    deeps += 1
    getUrl(urls)
    tags = getUrl(urls)
    urls = hrefBack(position)
    print 'Retrieving:', urls
