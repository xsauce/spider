#FileName:spider.py
#-*- coding:utf-8-*-
import spiderlib
import sys

if __name__ == '__main__':
	if sys.argv[1].startswith('-'):
		option=sys.argv[1][1:]
		if option=='s':
			simply_spider(sys.argv[2])
		elif option=='c':
			cookie_spider(sys.argv[2])
		elif option=='d':
			debug_spider(sys.argv[2])
		elif option=='b':
			bs_spider(sys.argv[2])
		elif option=='h':
			print '''
The parameters of this web spider program:
	s:simply_spider
	p:postdata_spider
	g:getdata_spider
	c:cookie_spider
	d:debug_spider
	b:bs_spider'''
		else:
			print 'Unknown option.'
		sys.exit()
