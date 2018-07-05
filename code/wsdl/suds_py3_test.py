from suds.client import Client

if __name__ == '__main__':
    client = Client('http://127.0.0.1:8002/demo/api?wsdl')
    result = client.service.getName('bob')
    print(result)
