import configparser


class IConfig():

    def getHost(self):
        return 123
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    print(config.sections())
    req_data = config['DEFAULT']['data_req']
    SERVER_ACCOUNT = config['SERVER_ACCOUNT']
    print(SERVER_ACCOUNT.get('userid'))
    print(SERVER_ACCOUNT.get('smtapp2018'))

    print(IConfig().getHost())



