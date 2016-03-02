from abc import ABCMeta, abstractmethod
from alert_state import AlertState
from alert import Alert


class Watchman(metaclass=ABCMeta):
    """A watchman watches for an undesirable incident."""
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def outpost(self) -> int:
        """This method has to be implemented by a child to watch over a certain
        metric.

        This will be called in the program's loop."""
        return AlertState.black

    @abstractmethod
    def get_last_alert(self) -> Alert:
        """This method has to be implemented by a child to return the last
        alert happened"""
        return None
