#-*- coding: utf-8 -*-
# exchange_rate.py
import spiderlib as sp
from bs4 import BeautifulSoup
import re

url='http://qq.ip138.com/hl.asp'
def get_money_sort_list():
	resp=sp.simply_spider(url)
	if resp:
		soup=BeautifulSoup(resp.read())
		try:
			sort_list=[ (op['value'],op.get_text()) for op in soup.select('#from')[0].find_all('option')]
			return dict(sort_list)
		except Exception,e:
			print e

def get_exchange(from_m,to_m,num):
	data={'from':from_m,'to':to_m,'q':num}
	resp=sp.getdata_spider(url,data)
	if resp:
		soup=BeautifulSoup(resp.read())
		try:
			rs_tr=soup.find_all('tr',attrs={'bgcolor':'#f6f6f6'})[0].find_next('tr')
			rs_list=[]
			for t in rs_tr:
				rs_list.append(t.get_text())
			data['exchange']=rs_list[1]
			data['tonum']=rs_list[2]
			print '%(q)s %(from)s X %(exchange)s = %(tonum)s %(to)s' % data
			return tuple(rs_list)
		except Exception,e:
			print e

if __name__ == '__main__':
    money_sorts=get_money_sort_list()

    while True:
    	cmd=raw_input('Input the Command >> ') or None
    	if cmd=='q' or cmd==None:break
    	if cmd=='ms':
    		for key,value in money_sorts.items():
    			print key,' ',value
    	else:
	    	try:
	    		money_names=money_sorts.keys()
	    		cmd_list=cmd.split(' ')
		        if len(cmd_list)!=3:
		    		raise Exception('parameters format style is not right, right example: USD CNY 100')
		    	if not(cmd_list[0] in money_names):
		    		raise Exception(cmd_list[0]+' is not be found,Input Command ms, Check Right Money Name')
		    	if not(cmd_list[1] in money_names):
		    		raise Exception(cmd_list[1]+' is not be found,Input Command ms, Check Right Money Name')
		    	get_exchange(cmd_list[0],cmd_list[1],float(cmd_list[2]))

	        except Exception,e:
		    	print e