import etcd3

if __name__ == '__main__':
    etcd = etcd3.client()
    events_iterator ,cancel= etcd.watch_prefix('/GRPC/roomserver')
    for event in events_iterator:
        print(event)

    # etcd_minoter.watch()
    # etcd_minoter.put('foo')