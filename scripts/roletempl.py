from dataclasses import dataclass

@dataclass
class RoleTempl:
    id: int
    name: str
    base_health: int
    base_attack: int
    base_defense: int
    base_speed: int
    