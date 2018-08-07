import xmltodict
from pip._vendor import requests

sturl = "http://api.nbws.gov.cn/ServiceTrans.asmx/Serviceprocessing"
if __name__ == '__main__':
    # client = Client(sturl)
    # result = client.service.Serviceprocessing(para='bob')
    req = requests.post(sturl, data={"para": """<?xml version="1.0" encoding="utf-8" ?>
<body>
<head>
<userid>smtapp</userid>
<password>smtapp2018</password>
</head>
<request>
<trans_no>SG0001</trans_no>
<resources_type></resources_type>
<hospital_name>医院</hospital_name>
<area_code></area_code>
</request>
</body>"""})

    print(req.status_code)
    print(req.encoding)
    print(req.text)
    print(req.content)
    print(str(req.content, 'utf-8'))
    print(requests.utils.get_unicode_from_response(req))

    res_xml = xmltodict.parse(req.text)
    real_xml = res_xml['string']['#text']
    print(real_xml)
    real_xml = xmltodict.parse(real_xml)
    # print(str_xml.get('string'))
    print(123)
# print(result)
