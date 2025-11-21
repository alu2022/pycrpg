from .fight import Fight
from .fightcontext import FightContext
from . import fightevents

class FightWithActQueue(Fight):
    def simulate(self) -> list[dict]:
        context = FightContext(self.seed, self.init_teams)
        
        context.log_action("begin_fight", {})
        context.dispatch_event(fightevents.BeginFight())
        
        while context.check_winner() == 0:
            actor = context.act_queue.get_current_role()
            self._on_turn(actor, context)
            context.act_queue.next_turn()

        winner = context.check_winner()
        context.log_action("end_fight", {"winner": winner})

        return context.actions
    