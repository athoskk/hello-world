#!/usr/bin/python

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

def getlink(html):
    reg = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
    linklst = re.findall(reg, html)
    for url in linklst:
        print url

html = getHtml("http://")

print getlink(html)
