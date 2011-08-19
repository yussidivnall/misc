#!/usr/bin/python
import urllib
import simplejson
#http://dcortesi.com/2008/05/28/google-ajax-search-api-example-python-code/
query = urllib.urlencode({'q' : 'bats'})
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' \
  % (query)
search_results = urllib.urlopen(url)
json = simplejson.loads(search_results.read())
results = json['responseData']['results']
for i in results:
  print i['title'] + ": " + i['url']

