import requests
from lxml import etree

# from pyquery import PyQuery as pq

# d = pq("<html></html>")
# d = pq(etree.fromstring("<html></html>"))
# d = pq(url='http://gtog.ningbo.gov.cn/col/col1894/index.html')
# # d = pq(filename="path_to_html_file")
# print(d)
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection':'keep-alive',
    'Content-Length': '24',
    'Content-Type': 'application/x-www-form-urlencoded',
    #Cookie: sidebar_collapsed=false; event_filter=all; _gitlab_session=feb1ccf88ec09763e1d2b7e4a6fec7d5; _yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjE4LCJpYXQiOjE1NzA2MDUxNzAsImV4cCI6MTU3MTIwOTk3MH0.uCshjR0WJH_Sv5zpEYjSJf8u7amkxZ9I3BNBFRyj3cY; _yapi_uid=18; acw_tc=2f624a5415706971080914934e34683ee1b6c977748e79026925aee671524b; UM_distinctid=16db4d7d9f4252-09e9cccb1ad5dd-67e1b3f-1fa400-16db4d7d9f54c9; CNZZDATA4478442=cnzz_eid%3D1458118261-1570693933-%26ntime%3D1570693933; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1570697108; csrftoken=UgOkzmVQCpWa3XCXVedeiW3ghRp2wSMkFgeywQgKY9TZluT6jaVbTNDcLgeSaBNL; sessionid=tqgyt1qfphug72byah1xsdqg79a23xw5; .ASPXANONYMOUS=tM4aF9m11QEkAAAAMTY3N2Y1YTItNzk4MS00MzM4LWJhZWYtNGE0YjI0Yzg5Y2FhHrvF6E054H-U3EVhAWFcIb_wuG01; ASP.NET_SessionId=u4e0i0rzwwp50uriqe4peu5i; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1570697893
    # 'Host': '112.13.89.101:9511',
    # 'Origin': 'http://112.13.89.101:9511',
    'Pragma': 'no-cache',
    # 'Referer': 'http://112.13.89.101:9511/v1/app/common/wjx/?url=https://www.wjx.cn/jq/47181953.aspx',
    'Referer': 'https://www.wjx.cn/jq/47181953.aspx',
    'Origin': 'https://www.wjx.cn',
    'Host': 'www.wjx.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36}'
}
# headers = {}
# print()

html_content = requests.post("http://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=47181953&t=1570698170334&starttime=2019%2F10%2F10%2016%3A35%3A10&ktimes=22&rn=1015602263.95446321&hlv=1&jqnonce=9da2b9a7-c867-44b2-97d7-b8d051e29606&jqsign=%3Bfc0%60%3Bc5%2Fa%3A45%2F66%600%2F%3B5f5%2F%60%3Af273g0%3B424", headers=headers,data={"submitdata":'1$1}2$1'} ).content.decode(
    'utf-8')
print(html_content)

#
# def i_req(url):
#     return requests.get(url, headers=headers, ).content.decode('utf-8')


if __name__ == '__main__':
    print(html_content)