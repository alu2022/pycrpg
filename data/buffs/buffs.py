from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from scripts.buff import Buff, BuffTempl
    from scripts.fightcontext import FightContext
    from scripts.fightrole import FightRole
else:
    from buff import Buff, BuffTempl
    from fightcontext import FightContext
    from fightrole import FightRole

class DamageBeinTurn(Buff):
    def __init__(self, template: BuffTempl, caster: FightRole, stack: int = 1, duration: int = 1, /,
                 k: float = 1.0, base_stat: str = "attack"):
        super().__init__(template, caster, stack, duration)
        self.k = k
        self.base_stat = base_stat

    def on_begin_turn(self, actor: FightRole, context: FightContext):
        damage = self.caster.calc_damage(self.k, self.base_stat)
        context.deal_damage(self.caster, actor, self, damage)

class Slowdown(Buff):
    def on_add(self, actor: FightRole, context: FightContext):
        speed = 0.5 * actor.base_stats.get("speed")
        actor.stats.add("speed",speed)
    def on_remove(self, actor: FightRole, context: FightContext):
        speed = actor.base_stats.get("speed")
        actor.stats.add("speed",speed)

class Frozen(Buff):
    def on_add(self, actor: FightRole, context: FightContext):
        actor.add_state("frozen")
    def on_remove(self, actor: FightRole, context: FightContext):
        actor.remove_state("frozen")