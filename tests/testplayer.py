import sys
import os
sys.path.append(os.getcwd())

from scripts.roletempl import RoleTemplMan
from scripts.skilltempl import SkillTemplMan
from scripts.bufftempl import BuffTemplMan
from scripts.role import Role
from scripts.player import Player
from scripts.gameconfig import GameConfig
import random
import json

def save_player(player: Player):
    os.makedirs(f"user/players", exist_ok=True)
    with open(f"user/players/{player.uid}.json", "w", encoding="utf-8") as f:
        json.dump(player.to_saved(), f, indent=4)

def load_player(uid: str) -> Player:
    with open(f"user/players/{uid}.json", "r", encoding="utf-8") as f:
        return Player.from_saved(json.load(f))

if __name__ == "__main__":
    RoleTemplMan.load("data/roles.json")
    SkillTemplMan.load("data/skills.json")
    BuffTemplMan.load("data/buffs.json")

    player =  Player("Test Player")
    print(f"player: {player.uid}, name={player.name}, create_time={player.create_time}")

    role_ids = random.choices(RoleTemplMan.get_all_roles(), k=10)
    for tid in role_ids:
        role = Role(tid)
        player.add_role(role)
        print(f"获得角色：{role.template.name}")

    print(f"level 1 need exp: {GameConfig.get_role_levelup_exp(1)}")
    for i in range(9, 100, 10):
        print(f"level {i} need exp: {GameConfig.get_role_levelup_exp(i)}")

    sum = 0
    for i in range(1, 100):
        sum += GameConfig.get_role_levelup_exp(i)
    print(f"sum exp to Lv.100: {sum}")

    role = player.role_collections.roles[0]
    exp = random.randrange(1, 100000)
    role.gain_exp(exp)
    print(f"角色 {role.template.name} 获得经验：{exp}，现在等级是 Lv.{role.level}({role.exp}/{GameConfig.get_role_levelup_exp(role.level)})")
    exp = random.randrange(1, 100000)
    role.gain_exp(exp)
    print(f"角色 {role.template.name} 获得经验：{exp}，现在等级是 Lv.{role.level}({role.exp}/{GameConfig.get_role_levelup_exp(role.level)})")

