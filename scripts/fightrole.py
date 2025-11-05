from role import Role

class FightRole:
    def __init__(self, role_info):
        self._role_info = role_info
        self._health = role_info.max_health
        self._buffers = []
