from typing import Any, Dict, List

class Event:
    listeners: Dict[str, List[Any]]

    def __init__(self):
        self.listeners = {}

    def invoke(self, event_id: str, *argv):
        for listener in self.listeners[event_id]:
            listener(argv)

    async def invoke_async(self, event_id: str, *argv):
        try:
            for listener in self.listeners[event_id]:
                await listener(argv)
        except KeyError:
            self.listeners[event_id] = []
            for listener in self.listeners[event_id]:
                await listener(argv)

    def add_listener(self, event_id: str, listener):
        try:
            self.listeners[event_id].append(listener)
        except KeyError:
            self.listeners[event_id] = []
            self.listeners[event_id].append(listener)