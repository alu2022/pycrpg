from role import Role
from roletempl import RoleTempl
from rolestats import RoleStats

class FightRole:
    def __init__(self, role: Role, team: int, field: int):
        self._uid = role.uid
        self._template = role.template
        self._stats = role.stats
        self._team = team
        self._field = field
        self._health = role.max_health
        self._buffs = []

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def template(self) -> RoleTempl:
        return self._template

    @property
    def stats(self) -> RoleStats:
        return self._stats

    @property
    def team(self) -> int:
        return self._team

    @property
    def field(self) -> int:
        return self._field

    @property
    def health(self) -> int:
        return self._health

    @property
    def is_alive(self) -> bool:
        return self._health > 0

    def take_damage(self, value: int):
        if value < 0:
            raise ValueError("Damage value must be non-negative.")
        self._health -= value

    def take_heal(self, value: int):
        if value < 0:
            raise ValueError("Heal value must be non-negative.")
        self._health += value
