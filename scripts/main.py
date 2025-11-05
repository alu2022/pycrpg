

class RoleTemplMan:
    pass

class Role:
    def __init__(self):
        pass

    @classmethod
    def create_default(cls, templ):
        self

class FightRole:
    def __init__(self, role = None):
        self.role = role

    @classmethod
    def from_role(cls, role):
        fightRole = cls(role)
        return fightRole

class FightAction:
    pass

class Fight:
    def add_role(self):


    def simulate(self) -> list[FightAction]:
        return []

if __name__ == "__main__":
    fight = Fight()


    actions = fight.simulate()

    for action in actions:
        print(action)

