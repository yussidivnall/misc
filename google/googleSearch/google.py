#!/usr/bin/python
import urllib2
import simplejson
import sys
import string
query=""
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
	url = ('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='+query)
	print url
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	results = simplejson.load(response)
	dump_results(results)
def parseArguments():
	global query
	for i in range(1,len(sys.argv)):
		if query!="":
			query+="+"
		query=query+"\""+sys.argv[i]+"\""
def main():
	global query
	parseArguments()
	#search(query)

if __name__ == "__main__":
	main()
