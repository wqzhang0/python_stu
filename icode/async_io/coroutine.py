def consumer():
    r = ''
    while True:
        print('[COUNSUMER]  run')
        print('type%s' %type(r))
        n = yield r
        if not n:
            return
        print('[COUNSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
