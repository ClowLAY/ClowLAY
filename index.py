# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

blogUrl = 'https://blog.csdn.net/weixin_44806193/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}


def addIntro(f):
    txt = ''' 技术小白'''
    f.write(txt)


def addProjectInfo(f):
    txt = '''
### 开源项目  
- https://github.com/practise-project/slf4j  AOP切面使用slf4j记录日志
- https://github.com/practise-project/SpringSecurity SpringSecurity实现简单权限控制   

[查看更多](https://github.com/ClowLAY/)     
	'''
    f.write(txt)


def addBlogInfo(f):
    http = urllib3.PoolManager(num_pools=5, headers=headers)
    resp = http.request('GET', blogUrl)
    resp_tree = etree.HTML(resp.data.decode("utf-8"))
    html_data = resp_tree.xpath(".//div[@class='article-item-box csdn-tracking-statistics']/h4")
    f.write("\n### 我的博客\n")
    cnt = 0
    for i in html_data:
        if cnt >= 5:
            break
        title = i.xpath('./a/text()')[1].strip()
        url = i.xpath('./a/@href')[0]
        item = '- [%s](%s)\n' % (title, url)
        f.write(item)
        cnt = cnt + 1
    f.write('\n[查看更多](https://blog.csdn.net/weixin_44806193/)\n')


f = open('README.md', 'w+')
addIntro(f)
f.write('<table><tr>\n')
f.write('<td valign="top" width="50%">\n')

addProjectInfo(f)
f.write('\n</td>\n')
f.write('<td valign="top" width="50%">\n')
addBlogInfo(f)
f.write('\n</td>\n')
f.write('</tr></table>\n')
f.close
