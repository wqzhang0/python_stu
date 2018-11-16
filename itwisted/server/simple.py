from twisted.web import server, resource
from twisted.internet import reactor, endpoints
from twisted.web.resource import EncodingResourceWrapper
from twisted.web.server import GzipEncoderFactory

#
# class Simple(resource.Resource):
#     isLeaf = True
#
#     def render_GET(self, request):
#         return '<html>Hello,world!</html>'
#
#
# site = server.Site(Simple())
# endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
# endpoint.listen(site)
# reactor.run()
#
#
#
#
# class Hello(resource.Resource):
#     isLeaf = True
#
#     def getChild(self, path, request):
#         if path == '':
#             return self
#         return resource.Resource.getChild(self,path,request)
#
#     def render_GET(self,request):
#         return "Hello, world! I am located at %r." % (request.prepath,)
# resource = Hello()
'''
or
root = Hello()
root.putChild('fred', Hello())
root.putChild('bob', Hello())
'''


class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>Hello, world!</html>"

resource = Simple()
wrapped = EncodingResourceWrapper(resource, [GzipEncoderFactory()])
site = server.Site(wrapped)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
endpoint.listen(site)
reactor.run()