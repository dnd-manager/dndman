from __future__ import annotations

from enum import Enum
from typing import Dict

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

class Character:
    portrait: str
    
    character_name: str
    player_name: str

    armor_class: int
    intiative: int
    speed: int
    hit_points: int

    strength_value = CharacterValue(EStrengthTypes.STRENGTH)
    dexerity_value = CharacterValue(EStrengthTypes.DEXTERITY)
    contitution_value = CharacterValue(EStrengthTypes.CONSTITUTION)
    intelligence_value = CharacterValue(EStrengthTypes.INTELLIGENCE)
    wisdom_value = CharacterValue(EStrengthTypes.WISDOM)
    charisma_value = CharacterValue(EStrengthTypes.CHARISMA)

    strength_saving_throw: int
    dexterity_saving_throw: int
    constitution_saving_throw: int
    intelligence_saving_throw: int
    wisdom_saving_throw: int
    charisma_saving_throw: int