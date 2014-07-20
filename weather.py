#FileName:weather.py
#-*- utf-8 -*-
from bs4 import BeautifulSoup
import string
import spiderlib
import re
import time

def dealStr(str):
    str=string.strip(str)
    str=str.replace(' ','')
    str=str.replace('\n','')
    str=str.replace('\r','')
    return str
def getWeahter():
    print time.strftime('%Y-%m-%d %H:%M:%S %a',time.localtime(time.time()))
    resp=spiderlib.simply_spider(r'http://www.weather.com.cn/html/weather/101020100.shtml')
    soup=BeautifulSoup(resp.read())
    w6h_list=soup.select('#weather6h .update table')

    for i in w6h_list:
        text=i.find_all('tr')
        wlist=[]
        wlist.append(text[0].get_text())
        wlist.append(text[2].get_text())
        wlist.append(text[3].get_text())
        wlist.append(text[4].get_text())
        wlist=map(dealStr,wlist)
        r=string.join(wlist,',')
        print r
if __name__ == '__main__':
    flag=True
    while flag:
        command=raw_input('>>')
        if command=='q':
            flag=False
        elif command=='g':
            getWeahter()

    
    
    
