
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

# from twisted.internet import protocol, reactor
# class Echo(protocol.Protocol):
#     def dataReceived(self, data):
#         self.transport.write(data)
#
#     def connectionLost(self, reason=None):
#         print('connectionLost')



#
# class Echo(protocol.Protocol):
#
#     def __init__(self, factory):
#         self.factory = factory
#
#     def connectionMade(self):
#         self.factory.numProtocols = self.factory.numProtocols + 1
#         self.transport.write(
#             "Welcome! There are currently %d open connections.\n" %
#             (self.factory.numProtocols,))
#
#     def connectionLost(self, reason):
#         self.factory.numProtocols = self.factory.numProtocols - 1
#
#     def dataReceived(self, data):
#         self.transport.write(data)

#
# class EchoFactory(protocol.Factory):
#     def buildProtocol(self, addr):
#         return Echo()
#
# endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
# reactor.run()

from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class QOTD(Protocol):

    # def connectionMade(self):
        # self.transport.write("An apple a day keeps the doctor away\r\n")
        # self.transport.loseConnection()

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print("Server said:", data)
        # self.transport.loseConnection()


class QOTDFactory(Factory):
    def buildProtocol(self, addr):
        return QOTD()

# 8007 is the port you want to run under. Choose something >1024
endpoint = TCP4ServerEndpoint(reactor, 20001)
endpoint.listen(QOTDFactory())
reactor.run()

#
# def main():
#     """This runs the protocol on port 8000"""
#     factory = protocol.ServerFactory()
#     factory.protocol = Echo
#     reactor.listenTCP(20001,factory)
#     reactor.run()
#
# # this only runs if the module was *not* imported
# if __name__ == '__main__':
#     main()
