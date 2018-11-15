import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods, require_GET, require_POST


@login_required
@require_http_methods(['GET'])
def homepage(request):
    template_name = 'base_frame.html'
    return TemplateResponse(request, template_name)


@require_http_methods(['GET'])
def main(request):
    template_name = 'main.html'
    return TemplateResponse(request, template_name)


@require_http_methods(['GET', 'POST'])
def rpc_login(request):
    template_name = 'main.html'

    if request.method == 'POST':
        account = request.POST.get('account', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=account, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/manager/index")
        else:
            return TemplateResponse(request, template_name, {'tip': 'Invalid account'})
    else:
        return TemplateResponse(request, template_name, {'tip': 'Invalid account'})


@login_required
@require_http_methods(['GET'])
def rpc_list(request, node_path=None):
    # 获取列表
    template_name = 'rpc_module_list.html'
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
    return TemplateResponse(request, template_name, context)


@login_required
@require_GET
def rpc_detail(request, node_path=None):
    template_name = 'rpc_detail.html'

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

    return TemplateResponse(request, template_name, context)


@login_required
@require_POST
def rpc_update(request, node_path):
    template_name = 'rpc_detail.html'

    from grpc_microservice.etcd_minoter.etcd_manager import EtcdServer
    etcd = EtcdServer().etcd_client
    _p = '/GRPC' + '/' + node_path
    _v, _meta = etcd.get(_p)

    _v = _v.decode("utf-8")
    context = json.loads(_v, encoding='utf-8')

    context['dec'] = request.POST['dec']
    context['doc'] = request.POST['doc']
    context['weight'] = request.POST['weight']
    if request.POST.get('force', False) == '1':
        context['force'] = True
    else:
        context['force'] = False
    if request.POST.get('pro', False) == '1':
        context['pro'] = True
    else:
        context['pro'] = False
    if request.POST.get('offline', False) == '1':
        context['offline'] = True
    else:
        context['offline'] = False
    etcd.put(_p, json.dumps(context, ensure_ascii=False),lease=_meta.lease_id)

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
    return TemplateResponse(request, template_name, context)
