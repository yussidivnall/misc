#!/usr/bin/python
import gdata.docs.service
#from http://code.google.com/apis/gdata/articles/python_client_lib.html
client = gdata.docs.service.DocsService()
client.ClientLogin("USER@Gmail.com","Password")
feed = client.GetDocumentListFeed()
for e in feed.entry:
	print e.title.text
