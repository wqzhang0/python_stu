import etcd3
from etcd3.events import PutEvent, DeleteEvent

if __name__ == '__main__':
    etcd = etcd3.client()
    events_iterator ,cancel= etcd.watch_prefix('/GRPC')
    for event in events_iterator:
        print(event.key)
        if isinstance(event,PutEvent):
            print(str(event.value,encoding='utf-8'))
            print('放入')
        elif isinstance(event,DeleteEvent):
            print('删除')

    # etcd_minoter.watch()
    # etcd_minoter.put('foo')