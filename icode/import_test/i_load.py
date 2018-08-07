if __name__ == '__main__':
    online = True
    if online:
        from icode.import_test.online_config import HOST
        HOST = HOST
    else:
        from icode.import_test.dev_config import HOST

        HOST = HOST
    print(HOST)
