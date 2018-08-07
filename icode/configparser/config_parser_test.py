import configparser


def createIni():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45', 'Compression': 'yes',
                         'CompressionLevel': '9'}

    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']
    topsecret['Port'] = '50022'
    topsecret['ForwardX11'] = 'no'
    config['DEFAULT']['ForwardX11'] = 'yes'

    with open('example.ini', 'w') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    print(config.sections())  # []
    config.read('example.ini')
    print(config.sections())  # ['bitbucket.org', 'topsecret.server.com']
    topsecret = config['topsecret.server.com']
    print(topsecret['Port'], type(topsecret['Port']))  # 50022 <class 'str'>
    print(topsecret.getboolean('ForwardX11'))  # False
    print(topsecret['ForwardX11'])  # no
    paths = config["Paths"]
    print(paths)
    print(paths.get('home_dir'))
    print(paths.get('my_dir'))
    print(paths.get('my_pirtures'))

    print(config['FPath'].get('farovter'))

    arthur = config.options('Arthur')
    print(config.items('Arthur', 'my_dir'))
    print(arthur)
    # print(arthur.get('my_dir'))
