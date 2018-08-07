from nameko.containers import ServiceContainer
from nameko.rpc import rpc


class Service:
    name = 'service'

    @rpc
    def hello(self, name):
        return "service | Hello, {}!".format(name)


CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}
# create a container
container = ServiceContainer(Service, config=CONFIG)

# ``container.extensions`` exposes all extensions used by the service
service_extensions = list(container.extensions)

# start service
container.start()

# stop service
container.stop()
