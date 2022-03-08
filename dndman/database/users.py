from __future__ import annotations
from enum import Enum
from typing import Dict

class Character:
    portrait: str
    
    character_name: str
    player_name: str

    armor_class: int
    intiative: int
    speed: int
    hit_points: int

    strength_value: CharacterValue
    dexerity_value: CharacterValue
    contitution_value: CharacterValue
    intelligence_value: CharacterValue
    wisdom_value: CharacterValue
    charisma_value: CharacterValue

    strength_saving_throw: int
    dexterity_saving_throw: int
    constitution_saving_throw: int
    intelligence_saving_throw: int
    wisdom_saving_throw: int
    charisma_saving_throw: int

    
class CharacterValue:
    value: int
    modifier: int
    strength_type: EStrengthTypes

    def __init__(self, strength_type: EStrengthTypes):
        self.strength_type = strength_type

    def serialize(self) -> Dict[str, str]:
        return {"value": self.value, "modifier": self.modifier}

    @staticmethod
    def deserialize(inp: Dict[str, str]) -> CharacterValue:
        character_value = CharacterValue()
        character_value.value = inp["value"]
        character_value.modifier = inp["modifier"]
        return character_value

    def __repr__(self) -> str:
        return f"CharacterValue(value={self.value}, modifier={self.modifier})"

class SkillValue(CharacterValue):
    pass

class EStrengthTypes(Enum):
    STRENGTH = 0,
    DEXTERITY = 1,
    CONSTITUTION = 2,
    INTELLIGENCE = 3,
    WISDOM = 4,
    CHARISMA = 5;