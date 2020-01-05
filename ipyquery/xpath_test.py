from pprint import pprint

from lxml import etree

from ipyquery.quick_start import html_content, i_req

print(html_content)
host = "http://gtog.ningbo.gov.cn"


# select = html.xpath(
#     "/html/body/div[@id='barrierfree_container']//select[@id='govreport111']/child")
def get_opion(url="http://gtog.ningbo.gov.cn/col/col1894/index.html", this_name="2019年17期"):
    try:
        html_content = i_req(url)
    except Exception as e:
        print(e)
        get_opion(url,this_name)
    html = etree.HTML(html_content)
    get_page(html, this_name)

    options = html.xpath(
        "/html/body/div[@id='barrierfree_container']//select[@id='govreport111']//option")

    for opion in options:
        print(opion.text)
        print(f"{host}{opion.attrib['value']}")
        if opion.text not in CATE:
            CATE[opion.text] = f"{host}{opion.attrib['value']}"
            get_opion(f"{host}{opion.attrib['value']}", opion.text)


# 获取条目
def get_page(html, name):
    element_title = html.xpath(
        "/html/body/div[@id='barrierfree_container']/div/table[4]/tr/td[@id='mm2']/table[3]/tr/td[2]/table")

    for x in element_title:
        a = x.xpath('tr/td[2]/a')
        if a and len(a) > 0:
            a = a[0]
            print(a.text)
            print(a.attrib['href'])
            page = CATE.get(f"{name}_page", [])
            page.append({"name": a.text, "href": f"{host}{a.attrib['href']}"})
            CATE[f"{name}_page"] = page


CATE = {}

if __name__ == '__main__':
    get_opion()
    pprint(CATE)
    # get_page()
