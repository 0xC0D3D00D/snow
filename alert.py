from alert_state import AlertState


class Alert():
    def __init__(self):
        self._state = AlertState.black
        self._watcher_name = None
        self._message = None

    def set_state(self, state: int) -> None:
        self._state = state

    def get_state(self) -> int:
        return self._state

    def set_watcher_name(self, watcher_name: str) -> None:
        self._watcher_name = watcher_name

    def get_watcher_name(self) -> None:
        return self._watcher_name

    def set_message(self, message: str) -> None:
        self._message = message

    def get_message(self) -> str:
        return self._message

    def __str__(self):
        return "Watcher: %s\nState: %s\nMessage: %s" % \
               (self._watcher_name, self._state, self._message)
