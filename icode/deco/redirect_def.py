from functools import wraps

def tt():
    def decorate(func,stub_func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


    return decorate


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = '/Greeter/SayHello'
    self.SayHelloAgain = '/Greeter/SayHelloAgain'



def proxy(stub_func):

    def decorate(func,stub_func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


    return decorate


@proxy(GreeterStub(1))
def proxy_func():
    pass



proxy_func()