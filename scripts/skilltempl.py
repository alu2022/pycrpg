from dataclasses import dataclass
import json

@dataclass
class SkillTempl:
    id: str
    name: str
    desc: str
    cost: int
    cooldown: int
    entry: str

class SkillTemplMan:
    _templates: dict[str, SkillTempl] = {}

    @classmethod
    def load(cls, file: str):
        with open(file, "r", encoding="utf-8") as f:
            root = json.load(f)
            cls._templates = {}
            for data in root:
                template = SkillTempl(**data)
                cls._templates[template.id] = template
    
    @classmethod
    def save(cls, file: str):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(cls._templates.values(), f, indent=4)

    @classmethod
    def get(cls, id: str) -> SkillTempl | None:
        return cls._templates.get(id)
