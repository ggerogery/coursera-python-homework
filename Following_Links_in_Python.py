import urllib
from BeautifulSoup import *
import re
'''

Following Links in Python

In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. 
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat
the process a number of times and report the last name you find.
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
