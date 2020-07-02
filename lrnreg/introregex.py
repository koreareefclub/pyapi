#!/usr/bin/env python
import urllib.request
import re
print("where to search")
url=input()
print("we'll try to search" + str(url))
searchFor=input()
searchMe=urllib.request.urlopen(url).read().decode("utf-8")

if re.search(searchFor, searchMe):
    print("found a match")
else:
    print("no match")
    
