#-*- coding:utf-8 -*-
from spiderlib import TinySpider as TSP

def query_jd(q):
	spider=TSP(
		'http://search.jd.com/Search',
		method='get',
		data={'keyword':q,'enc':'utf-8'},
		header_add_items={'Host':'search.jd.com','Referer':'http://www.jd.com'}
	)
	result=spider.obtain_resp()
	f=open('r.html','w')
	f.write(result)
	f.close()
	

