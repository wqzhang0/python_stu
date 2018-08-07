from nameko.rpc import rpc
from nameko.runners import ServiceRunner
from nameko.testing.utils import get_container


class ServiceA:
    name = "service_a"

    @rpc
    def hello(self, name):
        return "service_a | Hello, {}!".format(name)


class ServiceB:
    name = "service_b"

    @rpc
    def hello(self, name):
        return "service_b | Hello, {}!".format(name)


# create a runner for ServiceA and ServiceB
runner = ServiceRunner(config={'AMQP_URI': "amqp://guest:guest@localhost"})
runner.add_service(ServiceA)
runner.add_service(ServiceB)

# ``get_container`` will return the container for a particular service
container_a = get_container(runner, ServiceA)

# start both services
runner.start()

# stop both services
# runner.stop()
