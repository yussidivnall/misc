#!/usr/bin/python
#A simple script to look up things in google, inspired by a friend's work
#Author: Yussi Divnal, 
#Date: 12/July/2010
#License: See GPL

import urllib2
import simplejson
import sys
import string
import array
query=""
BaseAddress="http://ajax.googleapis.com/ajax/services/search/web?v=1.0"
Options={
	'order':'reverse',
	'pages':'3-1',
	'fields':['title','content','url','visibleUrl'],
	'columns':'2'
}
def color_line(line,color):
	ES="\x1B["
	if color=="blue":
		return ES+"02;34m"+line+ES+"0m"
		#return ""+"\033[31;40m"+line+"\033[31;40m"+"0m"
	if color=="red":
		return ES+"02;31m"+line+ES+"0m"
def format_line(line):
	ES="\x1B["
	BOLD_BLUE="01;34m"
	BLUE_UNDERLINE="03;34m"
	ret = string.replace(line,"<b>",""+ES+BOLD_BLUE)
	ret = string.replace(ret,"</b>",ES+"0m")
	return ES+BLUE_UNDERLINE+ret+ES+"0m"

def format_title(line):
	ES="\x1B["
	RESET=ES+"0m"
	UNDERLINE_BLUE=ES+"04;34m"
	BOLD_BLUE=ES+"01;34m"
	ret=UNDERLINE_BLUE+line+RESET
	ret = string.replace(ret,"<b>",RESET+BOLD_BLUE)
	ret = string.replace(ret,"</b>",RESET+UNDERLINE_BLUE)
	return ret
def format_content(line):
	ES="\x1B["
	RESET=ES+"0m"
	BOLD=ES+"01;37m"
	ret=line
	ret = string.replace(ret,"<b>",""+BOLD)
	ret = string.replace(ret,"</b>",RESET)
	ret = string.replace(ret,"&quot;","\"")#&#39;
	ret = string.replace(ret,"&#39;","'")
	ret = string.replace(ret,"  ","\n")
	return ret
def format_url(line):
	return "\x1B["+"02;32m"+line+"\x1B["+"0m"
def format_cached(line):
	return "\x1B["+"01;34m"+line+"\x1B["+"0m"
def dump_results(results):
	for r in results['responseData']['results']:
		#print r['titleNoFormatting']
        	
		print format_title(r['title'])
		print format_content(r['content'])
		print format_url(r['url'])
		print color_line( r['visibleUrl'],"red")
		print "cache: "+format_cached(r['cacheUrl'])

        	#print r['unescapedUrl']
		print 


def search(query):
	print "Query:"
	print query
	url = ('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='+query)
	print url
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	results = simplejson.load(response)
	dump_results(results)

def get_query_addresses(query): # TODO use string templates
	query_addresses=list()
	ranges=string.split(Options['pages'],',')
	address=""
	for field in ranges:
		values=string.split(field,'-')
		if(len(values)==2):
			start=int(values[0])
			end=int(values[1])
			if(start>end):#needs to reverse order (4-1)
				for i in range(end,start+1)[::-1]:
					address=BaseAddress+"&q="+query+"&start="+str(i)
					query_addresses.append(address)
			else:
				for i in range(start,end+1):
					address=BaseAddress+"&q="+query+"&start="+str(i)
					query_addresses.append(address)
		if(len(values)==1):
			address=BaseAddress+"&q="+query+"&start="+values[0]
			query_addresses.append(address)
	return query_addresses

#TODO take formating from a styles dictionary instead of dedicated built it functions
#TODO handle all other fields
def print_entry(entry):
	print 
	for field in Options['fields']:
		if (field=='title'):print format_title(entry[field])
		if (field=='content'):print format_content(entry[field])	
		if (field=='url'):print format_url(entry[field])
		if (field=='visibleUrl'):print color_line(entry[field],"red")
		if (field=='cacheUrl'):print "cache: "+format_cached(entry[field])

def output_results(results):
	for result in results:
		if(Options['order']=='reverse'):
			for entry in result['responseData']['results'][::-1]:
				print_entry(entry)
		else:
			for entry in result['responseData']['results']:
				print_entry(entry)
def get_search_results(addresses):
	results=list()
	for address in addresses:
		print "address:"+address
		url=(address)
		request=urllib2.Request(url)
		response=urllib2.urlopen(request)
		result=simplejson.load(response)
		results.append(result)
	print results
	return results

def usage():
	print """
google.py [options] search_terms
searches google for search terms
Options:
	-h or --help			Display this help message
	-p=PAGES or --pages=PAGES	Sets a range of result pages from google, for example -p=1-3,7,15-9,99
	[Still unimplemented!!!]
	-o=ORDER or --order=ORDER	sets the order to display each page's entries, for example -o=reverse will display the most relevant entries at the bottom 
	-f=FIELDS or --fields=FIELDS	sets  the fields to display in that order [title,content,url,cache] 
	-r or --raw
	-c=N or --columns=N
	-s or --styles
	"""

def replaceSpaces(s):
	print "Argument:"+s
	ret=""
	ret = s.replace(' ','+')
	print "ret:"+ret
	return ret

def parseArguments():
	global query
	for i in range(1,len(sys.argv)):
		#TODO implement loads more options
		if (sys.argv[i]=="-h" or sys.argv[i]=="--help"):
			usage()
			exit(1)
		elif (sys.argv[i].startswith("-p=")or sys.argv[i].startswith("--pages=")):
			vals=string.split(sys.argv[i],"=")
			#TODO test validity (only numbers, "," and "-")
			Options['pages']=vals[1]
#		else:
#			if query!="":query+="+"
#			elif (sys.argv[i].startswith('\"')):
#				
#				query=query+" +"
#				#for v in range(i,sys.argv):
#				query=query+sys.argv[i]
#			else: query=query+"\""+sys.argv[i]+"\""
		q=replaceSpaces(sys.argv[i])
		query=query+"\""+q+"\""
	print query
def main():
	global query
	#TODO load defaults from file in ~/.googleSearchScript
	parseArguments()
	addresses=get_query_addresses(query)
	results=get_search_results(addresses)
	output_results(results)


	#print results
	#print addresses
	#search(query)

if __name__ == "__main__":
	main()
