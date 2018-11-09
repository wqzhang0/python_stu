import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views import generic

from django.views.decorators.http import require_http_methods


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'module_list'

    def get_queryset(self):
        return RpcModule.objects.filter(is_delete=False, super_module__isnull=True)


class ModuleList(generic.ListView):
    template_name = 'app/'


@require_http_methods(['GET'])
def rpc_list(request, node_path=None):
    # 获取列表
    template_name = 'rpc_module_list.html'
    context_object_name = 'module_list'
    template = loader.get_template(template_name)

    context = {
        'module_list': [{'name': '/kick', 'is_dir': True, 'path': '/RoomServer/kick', 'prefix': '/RoomServer'},
                        {'name': '/random', 'is_dir': True, 'path': '/RoomServer/kick', 'prefix': '/RoomServer'},
                        {'name': '/join/uuid123456', 'is_dir': False, 'path': '/RoomServer/kick',
                         'prefix': '/RoomServer'}],
    }

    return HttpResponse(template.render(context, request))
    # from grpc_microservice.etcd_minoter.etcd_manager import EtcdServer
    #
    # etcd = EtcdServer().etcd_client
    #
    # childrens = etcd.get_prefix('/GRPC')
    # server = {}
    # for value, _meta in childrens:
    #     _v = value.decode("utf-8")
    #     _path = _meta.key.decode("utf-8").replace('/GRPC', '').split('/')
    #     print(_path)
    # _module = _path[1]
    # _server_name = _path[2]
    # print('{} : {}  {}'.format(_v, _module, _server_name))


@require_http_methods(['GET'])
def rpc_detail(request, node_path=None):
    # 获取列表
    template_name = 'rpc_detail.html'
    context_object_name = 'module_list'
    template = loader.get_template(template_name)

    context = {"doc": None, "force": False, "dec": "", "weight": 100, "offline": False,
                "uuid": "86e9b1fc-e32e-11e8-80d3-488ad268fa53", "ip": "192.168.0.105", "port": "60864", "pro": True}


    return HttpResponse(template.render(context, request))
