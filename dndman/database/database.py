from __future__ import annotations

import flask_login

from typing import Dict, List, Any
from pathlib import Path
import json

from dndman.logger import logger
import logging

USERS_PATH = Path("./database/users.json")

logger.setLevel(logging.DEBUG)

logger.info("Initiallizing database...")


class UserNotFoundException(Exception):
    pass


class User(flask_login.UserMixin):
    password: str

    def __init__(self):
        super().__init__()

    def serialize(self) -> Dict[str, str]:
        return {"username": self.id, "password": self.password}

    @staticmethod
    def deserialize(inp: Dict[str, str]) -> User:
        user = User()
        user.id = inp["username"]
        user.password = inp["password"]
        return user

    def __repr__(self) -> str:
        return f"User(id={self.id}, password={self.password})"


class Database:
    __users: List[User]

    def __init__(self):
        if not USERS_PATH.exists():
            with open(USERS_PATH, "w") as f:
                json.dump({}, f)

        with open(USERS_PATH) as f:
            data: Dict[str, List[Any]] = json.load(f)
            self.deserialize(data)

        print(self.__users)

    def has_user(self, username: str) -> bool:
        try:
            self.get_user(username)
        except UserNotFoundException:
            return False
        return True

    def get_user(self, username: str) -> User:
        for user in self.__users:
            if user.id == username:
                return user

        raise UserNotFoundException

    def add_user(self, user: User):
        self.__users.append(user)
        self.commit()

    def commit(self):
        with open(USERS_PATH, "w") as f:
            json.dump(self.serialize(), f, indent=4)
        pass

    def serialize(self):
        return {
            "users": self.serialize_users()
        }

    def deserialize(self, data):
        try:
            self.__users = Database.deserialize_users(data["users"])
        except KeyError:
            pass

    def serialize_users(self) -> List[Dict[str, str]]:
        return list(map(lambda user: user.serialize(), self.__users));

    @staticmethod
    def deserialize_users(users) -> List[User]:
        return list(map(lambda user: User.deserialize(user), users));

database: Database = Database()
