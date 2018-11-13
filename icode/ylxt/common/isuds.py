import time
import xmltodict
from suds.client import Client
import logging
url = 'http://hddy.nbwjw.gov.cn/AuthenticateService.asmx?wsdl'
client = Client(url)

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
print(client)
# pprint.pprint(response)

data = xmltodict.unparse({'body': {'head': {'userid': 'smt', 'password': 'smt@123456','trans_no':'GZYZ001'}, 'request': {'GZYZ001':{'USERID':'ee2018','NAME':'测试','IDCARD':330624198902070937,'PHONE':'18868139981','SENDIP':'192.168.1.109',
                                                                                                                                    'SENDDATE':'2018-11-09 16:57:00','SENDDEVICE':'','SMSCODE':'123456','SENDTERMINAL':'smt'}}}})
print(data.replace('\n',''))
_c = 0
# while True:
print(client.service.Process(data.replace('\n','')))
    # time.sleep(0.2)
    # _c +=1
    # print(_c)
