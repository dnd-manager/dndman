from typing import Any, Dict, List

class Event:
    listeners: Dict[str, List[Any]]

    def __init__(self):
        self.listeners = {}

    def invoke(self, event_id: str, *argv):
        for listener in self.listeners[event_id]:
            listener(argv)

    def add_listener(self, event_id: str, listener):
        self.listeners[event_id].append(listener)