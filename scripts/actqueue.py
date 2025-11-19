from fightrole import FightRole

class _Act:
    def __init__(self, role: FightRole, pos: int = 0):
        self.role = role
        self.pos = pos
        self.lock = False

class ActQueue:
    def __init__(self):
        self.queue: list[_Act] = []
        self.end = 0

    def init(self, roles: list[FightRole]):
        for role in roles:
            self.add_role(role)
        self.end = 0
        for act in self.queue:
            speed = act.role.stats.get("speed")
            self.end = max(self.end, speed)
        self.next_turn()

    def add_role(self, role: FightRole, pos: int = 0):
        self.queue.append(_Act(role, pos))

    def remove_role(self, role: FightRole):
        for i, act in enumerate(self.queue):
            if act.role == role:
                self.queue.pop(i)
                break

    def get_current_role(self) -> FightRole:
        return self.queue[0].role

    def next_turn(self):
        if not self.queue:
            return
        self.queue[0].pos = 0
        # update end
        #self.end = 0
        #for act in self.queue:
        #    speed = act.role.stats.get("speed")
        #    self.end = max(self.end, speed)
        # move fastest
        min_time = 1000
        for act in self.queue:
            time = max(self.end - act.pos, 0) / act.role.stats.get("speed")
            min_time = min(min_time, time)
        for act in self.queue:
            if not act.lock:
                act.pos += round(min_time * act.role.stats.get("speed"))
        self.queue.sort(key=lambda act: act.pos, reverse=True)

    def advance(self, role: FightRole, percent: float):
        act = self._get_act(role)
        if not act.lock:
            act.pos += round(self.end * percent)
            act.pos = max(act.pos, self.end)
            act.pos = min(act.pos, 0)

    def lock(self, role: FightRole):
        act = self._get_act(role)
        act.lock = True

    def unlock(self, role: FightRole):
        act = self._get_act(role)
        act.lock = False

    def _get_act(self, role: FightRole) -> _Act:
        for act in self.queue:
            if act.role == role:
                return act
        raise ValueError("Role is not in this queue")
