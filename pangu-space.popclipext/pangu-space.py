# coding: utf-8
import pangu
import os
import urllib.parse

# By mousepotato @https://anotherbug.com
if __name__ == '__main__':
    query = os.environ['POPCLIP_URLENCODED_TEXT']
    # 增加 盘古之白
    res = pangu.spacing_text(urllib.parse.unquote(query))
    # 修改双引号为直角
    res = res.replace("“", "「").replace("”", "」")
    print(res)
