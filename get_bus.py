#-*- encoding: utf-8 -*-

import logging, sys, urllib
import bs4

url = 'http://www.bus-sagasu.com/searches/{}-{}/{}-{}-{}/sort:1/'.format(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
soup = bs4.BeautifulSoup(urllib.urlopen(url).read(),"lxml")

for result in soup.select("div.resultContent"):
  for title in result.select("div.title"):
    print title.text.strip(),
  for seat in result.select("td.seats"):
    print seat.text,
  for price in result.select("td.price"):
    print price.text,
  print ""
