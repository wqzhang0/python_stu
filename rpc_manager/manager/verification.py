from app.models import RolePermission


class valide():
    # 校验方法
    VERSION_V1 = 1
    VERSION_V2 = 2

    def __init__(self) -> None:
        super().__init__()
        self._valideV1 = valideV1()

    def handler(self, token, api):
        # 根据不同的版本进行校验处理
        _version, _token = self.parse_token(token)
        if _version == self.VERSION_V1:
            return self._valideV1.check_premission(_token, api)

    def parse_token(self, token):
        # token 格式
        # version   token
        # 2位       16位
        return token[:2], token[2:]

class valide_base():
    def check_ip(self):
        """
        对ip进行校验
        :return:
        """
        pass
class valideV1():

    def check_premission(self, token, api):
        try:
            RolePermission.objects.get(uuid=token, api_url=api)
        except RolePermission.DoesNotExist:
            return False
        return True
"""
校验 颁发给模块?开发
模块,每个模块都需要在控制面板中注册信息,不容易维护



对内集成,用户权限
"""