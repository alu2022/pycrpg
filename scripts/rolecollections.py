from .role import Role

class RoleCollections:
    def __init__(self):
        self.roles: dict[str, Role] = {}
    
    def add_role(self, role: Role):
        if role.uid in self.roles:
            raise IndexError(f"Role with UID '{role.uid}' already exists.")
        self.roles[role.uid] = role
        
    def remove_role(self, role: Role):
        self.roles.pop(role.uid)

    def get_role(self, uid: str) -> Role:
        role = self.roles.get(uid)
        if role is None:
            raise IndexError(f"Role with UID '{uid}' not exists.")
        return role
    