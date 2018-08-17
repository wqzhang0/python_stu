import zookeeper
handler = zookeeper.init('localhost:2181')
#0表示持久化的,1表示持久化+序号,2表示瞬时的,3表示瞬时加序号型的
zookeeper.create(handler,'/zkpython_create_node','mydata1')
