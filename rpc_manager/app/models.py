import uuid as uuid
from django.db import models


# Create your models here.

class BaseMode(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        return self.save()


class RpcModule(BaseMode):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="服务名称")
    desc = models.CharField(max_length=500, null=False, blank=False, verbose_name="服务描述")
    super_module = models.ForeignKey('RpcModule', null=True, verbose_name="父类模块", on_delete=models.PROTECT)

    class Meta:
        db_table = "rpc_module"

    def __str__(self):
        return self.name


class RpcApi(BaseMode):
    module = models.ForeignKey('RpcModule', null=True, verbose_name="父类模块", on_delete=models.PROTECT)
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="接口名称")
    url = models.CharField(max_length=100, null=False, blank=False, verbose_name="接口地址")
    desc = models.CharField(max_length=500, null=False, blank=False, verbose_name="接口描述")

    class Meta:
        db_table = "rpc_api"

    def __str__(self):
        return self.name


class RpcRole(BaseMode):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="唯一标识")
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="角色名称")
    desc = models.CharField(max_length=500, null=False, blank=False, verbose_name="角色描述")

    class Meta:
        db_table = "rpc_Role"

    def __str__(self):
        return self.name


class RolePermission(BaseMode):
    RpcRole = models.ForeignKey('RpcRole', verbose_name="角色", related_name='role_per', null=False,
                                on_delete=models.PROTECT)
    RpcApi = models.ForeignKey('RpcApi', verbose_name="接口名称", related_name='role_per', null=False,
                               on_delete=models.PROTECT)

    class Meta:
        db_table = "rpc_Role_Permission"
        unique_together = ('RpcRole', 'RpcApi')

    def __str__(self):
        return self.RpcRole.name + self.RpcApi.name
