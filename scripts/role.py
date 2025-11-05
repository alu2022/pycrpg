from roletempl import RoleTempl
from roletemplman import RoleTemplMan
import uuid

class Role:
    def __init__(self, tid: int, uid: str = str(uuid.uuid4())):
        template = RoleTemplMan.get(tid)
        if template is None:
            raise Exception(f"Invalid template ID '{tid}'.")

        self._template = template
        self._uid = uid
        self._level = 1
        self.exp = 0
    
    @property
    def uid(self) -> str:
        return self._uid

    @property
    def template(self) -> RoleTempl:
        return self._template
    
    @property
    def max_health(self) -> int:
        return self._template.base_health + (self._level - 1) * 10

    @classmethod
    def from_saved(cls, data: dict):
        role = cls(data["tid"], data["uid"])
        role._level = data["level"]
        role.exp = data["exp"]
        return role

    def to_saved(self) -> dict:
        return {
            "uid": self._uid,
            "tid": self._template.id,
            "level": self._level,
            "exp": self.exp
        }
