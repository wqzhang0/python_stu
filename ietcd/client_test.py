import etcd3

if __name__ == '__main__':
    etcd = etcd3.client()
    v = etcd.get('foo')
    print(etcd.get('foo'))
    etcd.watch()
    etcd.put('foo')