from __future__ import annotations

import flask_login

from typing import Dict, List, Any
from pathlib import Path
import json
import uuid

from dndman.logger import logger
import logging

USERS_PATH = Path("./database/database.json")
PFP_PATH = "/static/resources/users/"

logger.setLevel(logging.DEBUG)
logger.info("Initiallizing database...")


class UserNotFoundException(Exception):
    pass


class User(flask_login.UserMixin):
    username: str
    password: str
    pfp_path: str

    def __init__(self):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.pfp_path = PFP_PATH + "unknown_user.svg"

    # serialize user into a json object    
    def serialize(self) -> Dict[str, str]:
        return self.__dict__

    # deserialize user back into a python object from a json object
    @staticmethod
    def deserialize(inp: Dict[str, str]) -> User:
        user = User()
        user.__dict__.update(inp)
        return user

    def __repr__(self) -> str:
        return f"User(username={self.username}, id={self.id}, password={self.password}, pfp_path={self.pfp_path})"


class Database:
    __users: List[User]

    def __init__(self):
        self.reload_json()

    # load data from json
    def reload_json(self):
        if not USERS_PATH.exists():
            USERS_PATH.parent.mkdir(exist_ok=True)
            with open(USERS_PATH, "w") as f:
                json.dump({"users": []}, f)

        with open(USERS_PATH) as f:
            data: Dict[str, List[Any]] = json.load(f)
            self.deserialize(data)

    # check if user with username exist
    def has_user_with_username(self, username: str) -> bool:
        try:
            self.get_user_with_username(username)
        except UserNotFoundException:
            return False
        return True

    
    # get user with username
    # Exceptions: raises UserNotFoundException if not found
    def get_user_with_username(self, username: str) -> User:
        "Takes username, and returns user with that username."
        self.reload_json()
        for user in self.__users:
            if user.username == username:
                return user

        raise UserNotFoundException

    # check if user with id exist
    def has_user(self, id: str) -> bool:
        try:
            self.get_user(id)
        except UserNotFoundException:
            return False
        return True

    # get user with id
    # Exceptions: raises UserNotFoundException if not found
    def get_user(self, id: str) -> User:
        self.reload_json()
        for user in self.__users:
            if user.id == id:
                return user

        raise UserNotFoundException

    # add user to database
    # Side Effects: Causes Json Dump with new data
    def add_user(self, user: User):
        self.__users.append(user)
        self.commit()

    # dump data into database json
    def commit(self):
        with open(USERS_PATH, "w") as f:
            json.dump(self.serialize(), f, indent=4)
        pass

    # serialize all database objects into json
    def serialize(self):
        return {"users": self.serialize_users()}

    # deserializes all database objects from json
    def deserialize(self, data):
        try:
            self.__users = Database.deserialize_users(data["users"])
        except KeyError:
            pass

    # serialize users in database to json
    def serialize_users(self) -> List[Dict[str, str]]:
        return list(map(lambda user: user.serialize(), self.__users))

    # deserialize users in database from json
    @staticmethod
    def deserialize_users(users) -> List[User]:
        return list(map(lambda user: User.deserialize(user), users))


database: Database = Database()
