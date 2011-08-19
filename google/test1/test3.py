#!/usr/bin/python
import urllib
import simplejson

query = urllib.urlencode({q : wouldamon cortesi})
url = http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s
  % (query)
search_results = urllib.urlopen(url)
json = simplejson.loads(search_results.read())
results = json[ aresponseData][ aresults]
for i in results:
  print i[ itle] + ": " + i[url]
