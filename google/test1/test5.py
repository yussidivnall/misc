#!/usr/bin/python
import urllib2
import simplejson
import sys
# This example request includes an optional API key which you will need to
# remove or replace with your own key.
# Read more about why it's useful to have an API key.
# The request also includes the userip parameter which provides the end
# user's IP address. Doing so will help distinguish this legitimate
# server-side traffic from traffic which doesn't come from an end-user.
url = ('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=Python+Tutorial')

request = urllib2.Request(url)
response = urllib2.urlopen(request)

# Process the JSON string.
results = simplejson.load(response)
#print results
for r in results['responseData']['results']:
	#print r
	print "-----------------------------------"
	#print r['GsearchResultClass']
	print r['visibleUrl']
	print r['titleNoFormatting']
	print r['title']
	print r['url']
	print r['cacheUrl']
	print r['unescapedUrl']
	print r['content']
	#print "start:", r['start'],"label:", r['label']
#print results['responseData']['cursor']
#for result in results:
#	print result
# now have some fun with the results...
#print results.resposeData
