# get_sitemap
######一个自动爬取sitemap并保存到本地的脚本，基于python2.7

##说明
```
站长在管理站点的时候，为了方便爬虫爬取网页，可通过设置站点的sitemap并提交给站长平台，如百度站长平台、360站长平台。

在http://help.bj.cn网站(第三方网站)，可以输入站长的站点，选择sitemap格式后可以下载到本地，本项目是一个以post方式自动提交

站点到该平台，获取到sitemap文件
```
##使用方式
```
#git clone https://github.com/tm2018/get_sitemap.git
修改git_sitemap.py的配置
...
my_host = '域名/ip地址'
type = 'xml/html/txt'  #选择一种保存格式
dir = '/var/www/html/sitemap' #sitemap的下载路径，请确保路径存在
...

#python get_sitemap.py
```

