from role import Role
from rolecollections import RoleCollections
import uuid

class Player:
    def __init__(self, uid: str | None = None):
        self.uid = uid if uid else str(uuid.uuid4)
        self.role_collections = RoleCollections()
        
    def add_role(self, role: Role):
        self.role_collections.add_role(role)

    def remove_role(self, role: Role):
        self.role_collections.remove_role(role)

    def get_role(self, uid: str) -> Role:
        return self.role_collections.get_role(uid)

    def to_saved(self) -> dict:
        return {
            "uid": self.uid,
            "roles": [r.to_saved() for r in self.role_collections.roles.values()]
        }
    
    @classmethod
    def from_saved(cls, data: dict) -> "Player":
        player = Player(data["uid"])
        roles = data["roles"]
        for r in roles:
            role = Role.from_saved(r)
            player.add_role(role)
        return player
    