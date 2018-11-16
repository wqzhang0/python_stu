from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

from itwisted.client.body_producer import BytesProducer

def sendGet():
    agent = Agent(reactor)

    d = agent.request(b'GET', b'http://127.0.0.1:9001/anything', Headers({'User-Agent': ['Twisted Web Client Example']}),
                      None)


    def cbResponse(ignored):
        print('Respnse received')

    d.addCallback(cbResponse)

    def cbShutdown(ignored):
        reactor.stop()

    d.addBoth(cbShutdown)

    reactor.run()


def sendBody():
    agent = Agent(reactor)

    body = BytesProducer(b"hello, world")
    d = agent.request(b'POST', b'http://127.0.0.1:9001/post', Headers({'User-Agent': ['Twisted Web Client Example'],'Content-Type': ['text/x-greeting']}),
                      body)

    def cbResponse(ignored):
        print('Respnse received')

    d.addCallback(cbResponse)

    def cbShutdown(ignored):
        reactor.stop()

    d.addBoth(cbShutdown)

    reactor.run()