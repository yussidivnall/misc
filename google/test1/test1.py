#!/usr/bin/python
#from http://code.google.com/apis/base/docs/1.0/pythondevguide.html
import gdata.base.service
import gdata.service
import lxml.etree
from lxml.etree import ElementTree
#try:
#    from xml.etree import ElementTree 
#except ImportError:
#    from elementtree import ElementTree 
import atom 
import gdata.base
gb_client = gdata.base.service.GBaseService()  
q = gdata.base.service.BaseQuery()  

#q.feed = '/base/feeds/snippets'  
q.feed = '/data/feeds/snippets'
q['start-index'] = '1'  
q['max-results'] = '10'  

q.bq = 'bats -Products -Produkte +Wildlife'
print q.ToUri()
#print q
feed = gb_client.QuerySnippetsFeed(q.ToUri())
for entry in feed.entry:
	print "------------------------"
	print entry.title.text	
	for n in entry.author:
		print n.name.text
	print entry.content.text
	print "Categories:"
	for c in entry.category:
		print c
	#print entry.author.name
	#print entry 
