import xml.etree.ElementTree as ET
import urllib
import re
'''
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geoxml.py. 
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract 
the comment counts from the XML data, compute the sum of the numbers in the file.
'''
address = raw_input('Enter location: ')
xml = urllib.urlopen(address).read() # open url and read the data

print 'Retrieved', str(address)
print 'Retrieved',len(xml),'characters'

tree = ET.fromstring(xml) # make xml tree
comment = tree.findall('comments/comment') # find path to 'count' values
sums = list()
count = 0
for name in comment: 
    numb = int(name.find('count').text)
    sums.append(numb)
    count += 1
print 'Count: ', count
print 'Sum: ', sum(sums)
