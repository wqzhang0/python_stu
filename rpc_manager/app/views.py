from django.shortcuts import render

# Create your views here.
from django.views import generic

from django.views.decorators.http import require_http_methods


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'module_list'

    def get_queryset(self):
        return RpcModule.objects.filter(is_delete=False,super_module__isnull=True)

class ModuleList(generic.ListView):
    template_name = 'app/'

@require_http_methods(['GET','POST'])
def rpc_list(request):
    # 获取列表
    from grpc_microservice.etcd_minoter.etcd_manager import EtcdServer

    etcd = EtcdServer().etcd_client

    childrens = etcd.get_prefix('/GRPC')
    server = {}
    for value, _meta in childrens:
        _v = value.decode("utf-8")
        _path = _meta.key.decode("utf-8").replace('/GRPC', '').split('/')
        print(_path)
        # _module = _path[1]
        # _server_name = _path[2]
        # print('{} : {}  {}'.format(_v, _module, _server_name))


    a = request.content_params
    pass