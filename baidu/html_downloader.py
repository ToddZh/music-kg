import requests
# from bs4 import BeautifulSoup
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        #            'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9,image/webp, * / *;q = 0.8'}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Content-Encoding': 'deflate'}
        response = requests.get(url,headers=headers,timeout=10)
        # response.encoding = 'utf-8'
        if response.status_code != 200:
            return None
        # response = BeautifulSoup(response.text, 'lxml')
        return response.content


