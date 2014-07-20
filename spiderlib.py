#FileName:spiderlib.py
#-*- coding:utf-8-*-

import urllib2
from urllib2 import Request,urlopen,URLError,HTTPError
import urllib
import cookielib

def cookie_spider(url):
	cookie=cookielib.CookieJar()
	cookieHandler=urllib2.HTTPCookieProcessor(cookie)
	opener=urllib2.build_opener(cookieHandler)
	urllib2.install_opener(opener)
	simply_spider(url)

def debug_spider(url):
	httpHandler=urllib2.HTTPHandler(debuglevel=1)
	httpsHandler=urllib2.HTTPSHandler(debuglevel=1)
	opener=urllib2.build_opener(httpHandler,httpsHandler)
	urllib2.install_opener(opener)
	resp=simply_spider(url)
	f=open('test.html','w')
	f.write(resp.read())
	f.close()

class TinySpider:
	url=''
	header_add_items={}
	data={}
	method='get' #get or post
	def __init__(self,url,**options):
		self.url=url
		self.header_add_items=options.get('header_add_items',{})
		self.data=options.get('data',{}) 
		self.method=options.get('method','')

	def obtain_resp(self):
		headers={'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36'}
		headers.update(self.header_add_items)
		if self.method=='post':
			req=Request(url=self.url,headers=headers,data=self.data)
		elif self.method=='get':
			full_url=self.url+urllib.urlencode(self.data)
			req=Request(url=full_url,headers=headers)
		else:
			req=Request(url=self.url,headers=headers)
		try:
			response=urlopen(req)
		except HTTPError,e:
			print 'HTTPError# code:',e.code
		except URLError,e:
			print 'URLError# reason:',e.reason
		else:
			return response.read()







def simply_spider(url,**header_add_items):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36'}
	headers.update(header_add_items)
	req=Request(url=url,headers=headers)
	try:
		response=urlopen(req)
	except HTTPError,e:
		print 'HTTPError# code:',e.code
	except URLError,e:
		print 'URLError# reason:',e.reason
	else:
		return response
