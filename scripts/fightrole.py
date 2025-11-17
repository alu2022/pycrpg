from __future__ import annotations
from typing import TYPE_CHECKING
from role import Role
from fightskill import FightSkill, FightSkillMan
if TYPE_CHECKING:
    from fightcontext import FightContext

class FightRole:
    def __init__(self, role: Role, team: int, field: int):
        self.uid = role.uid
        self.template = role.template
        self.team = team
        self.field = field
        self.base_stats = role.get_stats()
        self.stats = self.base_stats.copy()
        self.health = self.stats.get("health")
        self.states: dict[str, int] = {}
        self.buffs = []
        self.skills: list[FightSkill] = []
        for skill in role.skills:
            self.skills.append(FightSkillMan.load(skill))

    def is_alive(self) -> bool:
        return self.health > 0
    
    def add_state(self, state: str):
        if state in self.states:
            self.states[state] += 1
        else:
            self.states[state] = 1

    def remove_state(self, state: str):
        if state in self.states:
            self.states[state] -= 1
            if self.states[state] == 0:
                self.states.pop(state)

    def has_state(self, state: str) -> bool:
        return state in self.states
    
    def can_act(self) -> bool:
        if not self.is_alive():
            return False
        for state in [ "dizzy", "frozen" ]:
            if self.has_state(state):
                return False
        return True
    
    def prepare_fight(self, context: FightContext):
        for skill in self.skills:
            skill.prepare_fight(self, context)

    def calc_damage(self, context: FightContext, k: float) -> int:
        damage = round(self.stats.get("attack") * k)
        if context.random.random() < (self.stats.get("critical_changce") / 100):
            damage = round(damage * (1.0 + self.stats.get("critical_damage") / 100))
        return damage

    def take_damage(self, value: int) -> int:
        if value < 0:
            raise ValueError("Damage value must be non-negative.")
        reduce = 200 / (200 + self.stats.get("defense"))
        damage = max(1, round(value * reduce))
        self.health -= damage
        return damage
    
    def select_cast_skill(self, context: FightContext) -> FightSkill | None:
        for skill in self.skills:
            if skill.can_cast(self, context):
                return skill
        return None

    def on_begin_turn(self):
        for skill in self.skills:
            skill.update_cooltime()
        for buff in self.buffs:
            # TODO buff.on_begin_turn()
            pass

    def on_end_turn(self):
        for buff in self.buffs:
            # TODO buff.on_end_turn()
            pass
