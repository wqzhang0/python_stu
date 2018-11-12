import pprint

import requests

# _d = '"<?xml version="1.0" encoding="utf-8"?> <body><head><userid>smt</userid><password>smt@123456</password><trans_no>GZYZ001</trans_no></head><request><GZYZ001><USERID>ee2018</USERID><NAME>测试</NAME><IDCARD>330624198902070937</IDCARD><PHONE>18868139981</PHONE><SENDIP>192.168.1.109</SENDIP><SENDDATE>2018-11-12 11:37:00</SENDDATE><SENDDEVICE></SENDDEVICE><SMSCODE>123456</SMSCODE><SENDTERMINAL>smt</SENDTERMINAL></GZYZ001></request></body>"'
# _d = '"<?xml version="1.0" encoding="utf-8"?> <body><head><userid>smt</userid><password>smt@123456</password>
# <trans_no>GZYZ001</trans_no></head><request><GZYZ001></GZYZ001></request></body>"'
import xmltodict
data = xmltodict.unparse({'body': {'head': {'userid': 'smt', 'password': 'smt@123456','trans_no':'GZYZ001'}, 'request': {'GZYZ001':{'USERID':'ee2018','NAME':'测试','IDCARD':330624198902070937,'PHONE':'18868139981','SENDIP':'192.168.1.109',
                                                                                                                                    'SENDDATE':'2018-11-09 16:57:00','SENDDEVICE':'','SMSCODE':'123456','SENDTERMINAL':'smt'}}}})
print(data.replace('\n',''))
# _d = 'sdf'
_d = data.replace('\n','').replace('<','&lt;')
_d = _d.replace('"','&quot;')
_d = _d.replace('>','&quot;')

# _d = 'sdf'
request_body = ('''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Process xmlns="http://tempuri.org/">
      <XmlString>\''''
                + _d
                + '''\'</XmlString>
    </Process>
  </soap:Body>
</soap:Envelope>''').encode('utf-8')

request_headers = {'Post': 'AuthenticateService.asmx',
                   'Host': 'hddy.nbwjw.gov.cn',
                   'Content-Type': 'text/xml; charset=utf-8',
                   'Content-Length': str(len(request_body)),
                   'SOAPAction': 'http://tempuri.org/Process'}

# response = requests.post('http://hddy.nbwjw.gov.cn/AuthenticateService.asmx',
response = requests.post('http://hddy.nbwjw.gov.cn/AuthenticateService.asmx',
                         data=request_body, headers=request_headers)

request = response.request
print(response.status_code)
print(requests.utils.get_unicode_from_response(response))


# pprint.pprint(response)
