from __future__ import annotations

from enum import Enum
from typing import Dict
from .gameplay import DiceRoll

class CharacterValue:
    value: int
    modifier: int
    strength_type: EStrengthTypes

    def __init__(self, strength_type: EStrengthTypes):
        self.strength_type = strength_type

    def serialize(self) -> Dict[str, str]:
        return {"value": str(self.value), "modifier": str(self.modifier), "strength_type": self.strength_type.__repr__()}

    @staticmethod
    def deserialize(inp: Dict[str, str]) -> CharacterValue:
        character_value = CharacterValue(EStrengthTypes[inp["strength_type"]])
        character_value.value = int(inp["value"])
        character_value.modifier = int(inp["modifier"])
        return character_value

    def __repr__(self) -> str:
        return f"CharacterValue(value={self.value}, modifier={self.modifier})"

class SkillValue:
    proficient: bool
    value: int
    strength_type: EStrengthTypes

    def __init__(self, strength_type: EStrengthTypes):
        self.strength_type = strength_type

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
    max_hit_points: int
    current_hit_points: int
    hit_dice: DiceRoll

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