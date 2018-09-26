import json
from baidu import html_downloader

new_url='https://baike.baidu.com/item/%E5%91%A8%E6%9D%B0%E4%BC%A6'
downloader = html_downloader.HtmlDownloader()
data = downloader.download(new_url)
print(data)