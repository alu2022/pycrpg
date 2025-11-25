from typing import Callable

class EventMan:
    def __init__(self):
        self._listeners: dict[type, dict] = {}
        self._id: int = 0

    def register(self, event_type: type, callback: Callable[..., bool]) -> int:
        if event_type not in self._listeners:
            self._listeners[event_type] = {}
        self._id += 1
        self._listeners[event_type][self._id] = callback
        return self._id
    
    def unregister(self, id: int):
        for mapping in self._listeners.values():
            mapping.pop(id, None)

    def dispatch(self, event) -> bool:
        event_type = type(event)
        if event_type in self._listeners:
            for callback in self._listeners[event_type].values():
                if callback(event):
                    return True
        return False
