import requests

request_body = '''<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:ns1="http://tempuri.org/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Header/><ns0:Body><ns1:Process><ns1:XmlString>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;&lt;body&gt;&lt;head&gt;&lt;password&gt;smt@123456&lt;/password&gt;&lt;userid&gt;smt&lt;/userid&gt;&lt;trans_no&gt;GZYZ001&lt;/trans_no&gt;&lt;/head&gt;&lt;request&gt;&lt;GZYZ001&gt;&lt;SENDIP&gt;192.168.1.109&lt;/SENDIP&gt;&lt;NAME&gt;\xe6\xb5\x8b\xe8\xaf\x95&lt;/NAME&gt;&lt;SENDTERMINAL&gt;smt&lt;/SENDTERMINAL&gt;&lt;SENDDEVICE&gt;&lt;/SENDDEVICE&gt;&lt;USERID&gt;ee2018&lt;/USERID&gt;&lt;SENDDATE&gt;2018-11-09 16:57:00&lt;/SENDDATE&gt;&lt;PHONE&gt;18868139981&lt;/PHONE&gt;&lt;IDCARD&gt;330624198902070937&lt;/IDCARD&gt;&lt;SMSCODE&gt;123456&lt;/SMSCODE&gt;&lt;/GZYZ001&gt;&lt;/request&gt;&lt;/body&gt;</ns1:XmlString></ns1:Process></ns0:Body></SOAP-ENV:Envelope>
'''.encode('utf-8')

request_headers = {
    'Content-Type': 'text/xml'}

response = requests.post('http://hddy.nbwjw.gov.cn/AuthenticateService.asmx',
                         data=request_body, headers=request_headers)

request = response.request
print(response.status_code)
print(requests.utils.get_unicode_from_response(response))

# pprint.pprint(response)
