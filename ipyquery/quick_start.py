import requests
from lxml import etree

# from pyquery import PyQuery as pq

# d = pq("<html></html>")
# d = pq(etree.fromstring("<html></html>"))
# d = pq(url='http://gtog.ningbo.gov.cn/col/col1894/index.html')
# # d = pq(filename="path_to_html_file")
# print(d)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Cookie: BIGipServerpublic-shizhengfumenhu-80-pool=1830046218.20480.0000; Hm_lvt_7cb65dbe40a6c02096dd8f8dbf47a19f=1569391862,1569392010,1569392024,1569392042; openFlag=0; Hm_lpvt_7cb65dbe40a6c02096dd8f8dbf47a19f=1569392064
    'Host': 'gtog.ningbo.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://gtog.ningbo.gov.cn/col/col1791/index.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# print()

html_content = requests.get("http://gtog.ningbo.gov.cn/col/col1894/index.html", headers=headers, ).content.decode(
    'utf-8')


def i_req(url):
    return requests.get(url, headers=headers, ).content.decode('utf-8')


