import xmltodict
from suds.client import Client
url = 'http://hddy.nbwjw.gov.cn/AuthenticateService.asmx?wsdl'
client = Client(url)
data = xmltodict.unparse({'body': {'head': {'userid': 'smt', 'password': 'smt@123456','trans_no':'GZYZ001'}, 'request': {'GZYZ001':{'USERID':'ee2018','NAME':'测试','IDCARD':330624198902070937,'PHONE':'18868139981','SENDIP':'192.168.1.109',
                                                                                                                                    'SENDDATE':'2018-11-09 16:57:00','SENDDEVICE':'','SMSCODE':'123456','SENDTERMINAL':'smt'}}}})
print(client.service.Process(data))