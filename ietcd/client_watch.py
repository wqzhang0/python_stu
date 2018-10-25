import etcd3

if __name__ == '__main__':
    etcd = etcd3.client()
    etcd.put('/foo','bat')
    v = etcd.get('foo')
    print(etcd.get('foo'))
    print(etcd.get('/foo'))


    etcd.put
    # etcd.watch()
    # etcd.put('foo')