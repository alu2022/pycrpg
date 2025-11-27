from scripts.buff import Buff, BuffTempl
from scripts.fightcontext import FightContext
from scripts.fightrole import FightRole
from typing import override

class DamageBeinTurn(Buff):
    def __init__(self, template: BuffTempl, caster: FightRole, stack: int, duration: int, /,
                 k: float = 1.0, base_stat: str = "attack"):
        super().__init__(template, caster, stack, duration)
        self.k = k
        self.base_stat = base_stat

    @override
    def on_begin_turn(self, actor: FightRole, context: FightContext):
        damage = self.caster.calc_damage(self.k, self.base_stat)
        context.deal_damage(self.caster, actor, self, damage)

class StateBuff(Buff):
    def __init__(self, template: BuffTempl, caster: FightRole, stack: int, duration: int, /,
                 state: str):
        super().__init__(template, caster, stack, duration)
        self.state = state
    
    @override
    def on_add(self, actor: FightRole, context: FightContext):
        actor.add_state(self.state)
    
    @override
    def on_remove(self, actor: FightRole, context: FightContext):
        actor.remove_state(self.state)

class Statbuff(Buff):
    def __init__(self, template: BuffTempl, caster: FightRole, stack: int, duration: int, /,
                  stat: str, k: float = 1.0):
        super().__init__(template, caster, stack, duration)
        self.stat = stat
        self.k = k

    @override
    def on_add(self, actor: FightRole, context: FightContext):
        self.value = round(self.stack * self.k * actor.base_stats.get(self.stat))
        actor.stats.add(self.stat, self.value)

    @override
    def on_remove(self, actor: FightRole, context: FightContext):
        actor.stats.add(self.stat, -self.value)
