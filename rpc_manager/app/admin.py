from django import forms
from django.contrib import admin

# Register your models here.

from app.models import RpcModule, RpcApi, RpcRole, RolePermission


class RpcModuleInline(admin.StackedInline):
    model = RpcModule
    extra = 1


class RpcModuleForm(forms.ModelForm):
    super_module = forms.ModelChoiceField(queryset=RpcModule.objects.filter(is_delete=False), required=False)

    class Meta:
        model = RpcModule
        fields = ['super_module', 'name', 'desc']

    def __str__(self):
        return self.name

    # name = forms.CharField(max_length=200, required=True)
    # desc = forms.CharField(max_length=500, required=True)


class IsDeleteFilter(admin.SimpleListFilter):
    title = ('是否被删除')
    parameter_name = 'is_delete'

    def queryset(self, request, queryset):
        return queryset.filter(is_delete=self.value())

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            (True, "已删除"),
            (False, "未删除"),
        )


class RpcModuleAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = RpcModule.objects.filter(is_delete=False)
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    form = RpcModuleForm
    fieldsets = [
        (None, {'fields': ['super_module']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['desc']}),
    ]

    # q = RpcModule.objects.filter(is_delete=False)

    list_display = ('name', 'desc', 'super_module')

    # list_filter = [IsDeleteFilter]


# inlines = [RpcModuleInline]


class RpcApiAdmin(admin.ModelAdmin):
    fieldsets = [
    ]

    list_display = ('name', 'url', 'desc')


class RpcRoleForm(forms.ModelForm):
    class Meta:
        model = RpcRole

        fields = ['name', 'desc']

    def __str__(self):
        return self.name


class RpcRoleAdmin(admin.ModelAdmin):
    fieldsets = [
    ]

    form = RpcRoleForm
    list_display = ('uuid', 'name', 'desc')


class RolePermissionAdmin(admin.ModelAdmin):
    fieldsets = [
    ]

    list_display = ('RpcRole', 'RpcApi')


admin.site.register(RpcModule, RpcModuleAdmin)
admin.site.register(RpcApi, RpcApiAdmin)
admin.site.register(RpcRole, RpcRoleAdmin)
admin.site.register(RolePermission, RolePermissionAdmin)
