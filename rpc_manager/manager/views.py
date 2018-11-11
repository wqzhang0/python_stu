import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.views.decorators.http import require_http_methods, require_GET, require_POST


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'module_list'

    def get_queryset(self):
        return RpcModule.objects.filter(is_delete=False, super_module__isnull=True)


class ModuleList(generic.ListView):
    template_name = 'manager/'

@require_http_methods(['GET'])
def main(request):
    template_name = 'main.html'
    template = loader.get_template(template_name)
    return HttpResponse(template.render({}, request))


@require_POST
def rpc_login(request):
    if request.POST['account'] == 'wqzhang' and request.POST['password'] == '1':
        request.session['member_id'] = '1'
        return HttpResponseRedirect("/manager/list")
    else:
        template_name = 'main.html'
        template = loader.get_template(template_name)
        return HttpResponse(template.render({'tip': 'Invalid account'}, request))


@require_http_methods(['GET'])
def rpc_list(request, node_path=None):
    if request.session.get('member_id') != '1':
        template_name = 'main.html'
        template = loader.get_template(template_name)
        return HttpResponse(template.render({'tip': 'please login'}, request))

    # 获取列表
    template_name = 'rpc_module_list.html'
    template = loader.get_template(template_name)
    from grpc_microservice.etcd_minoter.etcd_manager import EtcdServer
    etcd = EtcdServer().etcd_client
    if not node_path:
        _p = '/GRPC'
    else:
        _p = '/GRPC' + '/' + node_path
    childrens = etcd.get_prefix(_p)
    module_list = []
    module_name_list = []

    # 过滤出 下一级
    for value, _meta in childrens:
        _path = _meta.key.decode("utf-8").replace(_p, '')
        _path_split = _path.split('/')
        if len(_path_split) > 1:
            if node_path:
                __p = node_path + "/" + _path_split[1]
            else:
                __p = _path_split[1]
            _info = {'name': _path_split[1], 'is_dir': False, 'path': __p}
            if len(_path_split) > 2:
                _info['is_dir'] = True
            if _path_split[1] not in module_name_list:
                module_name_list.append(_path_split[1])
                module_list.append(_info)

    # 上一层
    _pre = None
    module_name = None
    if node_path:
        __pre = node_path.split('/')
        if len(__pre) > 1:
            _pre = "/".join(__pre[:-1])
        module_name = node_path.split('/')[-1]
    context = {
        'module_name': module_name,
        'pre_module': _pre,
        'module_list': module_list,
    }
    return HttpResponse(template.render(context, request))


@require_GET
def rpc_detail(request, node_path=None):
    template_name = 'rpc_detail.html'
    template = loader.get_template(template_name)

    from grpc_microservice.etcd_minoter.etcd_manager import EtcdServer
    etcd = EtcdServer().etcd_client
    if not node_path:
        _p = '/GRPC'
    else:
        _p = '/GRPC' + '/' + node_path
    _v, _meta = etcd.get(_p)
    _v = _v.decode("utf-8")
    context = json.loads(_v, encoding='utf-8')
    # 上一层
    _pre = None
    module_name = None
    if node_path:
        __pre = node_path.split('/')
        if len(__pre) > 1:
            _pre = "/".join(__pre[:-1])
        module_name = node_path.split('/')[-1]
    context['module_name'] = module_name
    context['pre_module'] = _pre
    context['key'] = node_path

    return HttpResponse(template.render(context, request))


@require_POST
def rpc_update(request, node_path):
    template_name = 'rpc_detail.html'
    template = loader.get_template(template_name)

    from grpc_microservice.etcd_minoter.etcd_manager import EtcdServer
    etcd = EtcdServer().etcd_client
    _p = '/GRPC' + '/' + node_path
    _v, _meta = etcd.get(_p)
    _v = _v.decode("utf-8")
    context = json.loads(_v, encoding='utf-8')

    context['dec'] = request.POST['dec']
    context['doc'] = request.POST['doc']
    context['weight'] = request.POST['weight']
    context['force'] = request.POST.get('force', False)
    context['pro'] = request.POST.get('pro', False)
    context['offline'] = request.POST.get('offline', False)
    etcd.put(_p, json.dumps(context, ensure_ascii=False))

    _v, _meta = etcd.get(_p)
    _v = _v.decode("utf-8")
    context = json.loads(_v, encoding='utf-8')
    # 上一层
    _pre = None
    module_name = None
    if node_path:
        __pre = node_path.split('/')
        if len(__pre) > 1:
            _pre = "/".join(__pre[:-1])
        module_name = node_path.split('/')[-1]
    context['module_name'] = module_name
    context['pre_module'] = _pre
    context['key'] = node_path

    return HttpResponse(template.render(context, request))
