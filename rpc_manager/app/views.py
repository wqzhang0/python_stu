from django.shortcuts import render

# Create your views here.
from django.views import generic

from app.models import RpcModule


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'module_list'

    def get_queryset(self):
        return RpcModule.objects.filter(is_delete=False,super_module__isnull=True)

class ModuleList(generic.ListView):
    template_name = 'app/'
