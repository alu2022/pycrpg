from fightrole import FightRole
from fightaction import FightAction
from random import Random
import uuid

class FightContext:
    def __init__(self, seed: int):
        self.random = Random(seed)
        self.all_roles: list[FightRole] = []
        self.winner: int = 0
        self.round: int = 0
        self.actor_queue: list[FightRole] = []
        self.actor: FightRole | None = None

    def add_role(self, role: FightRole):
        self.all_roles.append(role)

class FightResult:
    def __init__(self):
        self.init_roles: list[FightRole] = []
        self.round: int = 0
        self.winner: int = 0
        self.actions: list[str] = []

class Fight:
    def __init__(self, seed: int = int(uuid.uuid4())):
        self.seed = seed
        self.random = Random(seed)
        self.all_roles : list[FightRole] = []
        self.winner: int = 0
        self._round: int = 0
        self._actor: FightRole | None = None
        self._actor_queue: list[FightRole] = self.all_roles.copy()
        self._actions: list[str] = []

    @classmethod
    def from_saved(cls, data: dict):
        fight = cls(data["seed"])
        fight.winner = data["winner"]
        # load init roles
        # load actions
    
    @property
    def round(self) -> int:
        return self._round
    
    @property
    def actor(self) -> FightRole | None:
        return self._actor

    @property
    def actor_queue(self) -> list[FightRole]:
        return self._actor_queue

    def add_role(self, role: FightRole):
        self.all_roles.append(role)

    def get_role(self, uid: str) -> FightRole:
        for role in self.all_roles:
            if role.uid == uid:
                return role
        raise ValueError(f"Role with uid '{uid}' not found.")
    
    def do_action(self, action: str):
        if action == "BeginRound":
            self._round += 1
            self._actor_queue = [role for role in self.all_roles if role.is_alive]
            self._actor_queue.sort(key=lambda x: x.stats.speed, reverse=True)
        if action == "EndRound":
            pass
        if action == "BeginTurn":
            self._actor = self._actor_queue.pop(0)
        if action == "EndTurn":
            self._actor = None
            self._actor_queue = [role for role in self._actor_queue if role.is_alive]
            self._actor_queue.sort(key=lambda x: x.stats.speed, reverse=True)
        self._actions.append(action)

    def simulate(self) -> int:
        self._actions.clear()

        # context = FightContext(self.seed)
        
        # copy init roles

        state = "BeginFight"
        while state != "EndFight":
            if state == "BeginFight":
                self._actions.append("BeginFight")

        
        return self.winner
    
    def get_actions(self) -> list[str]:
        return self._actions
    
    @classmethod
    def check_winner(cls, actors: list[FightRole]) -> int:
        winner: int = 0
        for role in actors:
            if role.is_alive:
                if winner == 0:
                    winner = role.team
                elif winner != role.team:
                    return 0
        return winner
    