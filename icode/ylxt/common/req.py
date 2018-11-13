import requests
import xmltodict


def getData(param, _url='http://api.nbws.gov.cn/ServiceTrans.asmx/Serviceprocessing',timeout=2):
    req = requests.post(_url, data={"para": convert2Para(param)}, timeout=timeout)

    print(requests.utils.get_unicode_from_response(req))

    res_xml = xmltodict.parse(req.text)
    real_xml = res_xml['string']['#text']
    real_xml = xmltodict.parse(real_xml)
    response = real_xml['body']['response']
    if response['ret_code'] != 0:
        print("ret_code Error:" + response['ret_code'])
    return response


def convert2Para(dict):
    data = xmltodict.unparse({'body': {'head': {'userid': 'smtapp', 'password': 'smtapp2018'}, 'request': dict}})
    return data




if __name__ == '__main__':
    xml = getData({'trans_no': 'SG0001', 'resources_type': '', 'hospital_name': ''})
    hospitals = xml['hospitals']['hospital']
    print(type(hospitals))
    for hospital in hospitals:
        org_id = hospital['org_id']
        hospital_id = hospital['hospital_id']
        hospital_info = getData({'trans_no': 'SG0002', 'hospital_id': hospital_id})
        print(hospital_info)
        break
        print(hospital['hospital_name'])
        print(hospital['hospital_address'])
        print(hospital['hospital_picture'])
        print(hospital['hospital_reg_status'])
        print(hospital['hospital_tel'])


