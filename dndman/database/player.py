from __future__ import annotations
from typing import Dict

class Character:
    portrait: str
    name: str
    player_name: str
    
    def serialize(self) -> Dict[str, str]:
        return {"username": self.id, "password": self.password, "pfp": self.pfp_path}

    @staticmethod
    def deserialize(inp: Dict[str, str]) -> Character:
        character = Character()
        return character

    def __repr__(self) -> str:
        return f"(id={self.id}, password={self.password}, pfp={self.pfp_path})"