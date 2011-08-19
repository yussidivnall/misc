#!/usr/bin/python
#from http://code.google.com/apis/base/docs/1.0/pythondevguide.html
import gdata.base.service
import gdata.service
import lxml.etree
from lxml.etree import ElementTree

client = gdata.base.service.GBaseService()
q = gdata.base.service.BaseQuery() 
q.feed = '/base/feeds/itemtypes/en_US' 
q.max_results = '1'
q.bq='cars for sale'
print q
feed = client.QueryItemTypesFeed (q.ToUri())
# List the item types and their attributes 
#print feed
#for entry in feed.entry:
#	print 'Item Type:', entry.title.text
#	print 'Attributes:'
#	for attribute in entry
#  print entry.attributes
#  for attribute in entry.attributes:
#    print '   %s (%s)' % (attribute.name, attribute.type)

