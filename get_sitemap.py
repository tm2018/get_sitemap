# -*- coding: utf-8 -*-
####自动生成sitemap地图脚本
import urllib2
import urllib
import os
import time

#此url可以生成sitemap
url = 'http://help.bj.cn/show.asp'
#目标域名，请设置成自己的域名
my_host = 'www.alewolf.com'
#支持的格式有xml,txt,html三种
type = 'xml'
#保存的目的路径
dir = '/var/www/html/sitemap'

#post提交的参数
formdata = {
            'domain': my_host,
            'charset': 'utf-8',
            'submit1': '生成',
            'changefreq': 'always',
            'priority': 0.5,
            'myherf': 'true',
            'aherf': 'true',
            'sitemap': 'true',
            'pcmob': '',
            'remob': ''
            }
header = {
            'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Cache-Control': 'max-age=0, no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '144',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'ASPSESSIONIDASACBBSD=GOFDFCCDL…7e371728653ccf1861=1535529072',
            'Host': 'help.bj.cn',
            'Pragma': 'no-cache',
            'Referer': 'http://help.bj.cn/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/60.0'
            }
try:
    data = urllib.urlencode(formdata)
    request = urllib2.Request(url,data,header)
    #注意，这里设置了超时，如果20s内未从远端服务器获取到response，则超时退出
    urllib2.urlopen(request,timeout=10)
    #网站生成sitemap需要一定的时间，所以等待5s
    time.sleep(5)
    
    filename = '%s.%s' %('sitemap',type)
    #拼接下载的url
    download_url = '%s/%s/%s.%s' %('http://help.bj.cn/download',my_host,'sitemap',type)

    #pwd = os.path.split(os.path.realpath(__file__))[0]
    os.chdir(dir)
    if os.path.exists(filename):
        os.remove(filename)
    #保存获取到的sitemap
    f = urllib2.urlopen(download_url)
    with open(filename, "wb") as file:
       file.write(f.read())
except urllib2.URLError as e:
    print '获取失败，失败原因：%s' %e
