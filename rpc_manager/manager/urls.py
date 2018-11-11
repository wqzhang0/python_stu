"""rpc_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    # path('module/', ),
    # path('index/',IndexView.as_view(template_name="index.html")),
    path('list', views.rpc_list,name='index'),
    path('login', views.rpc_login,name='login'),
    path('list/<path:node_path>', views.rpc_list,name='rpc_list'),
    path('detail/<path:node_path>', views.rpc_detail,name='rpc_detail'),
    path('update/<path:node_path>', views.rpc_update,name='rpc_update'),
    # detail
    # path('<path:node_path>/<path:node_path>', views.rpc_list),
]
