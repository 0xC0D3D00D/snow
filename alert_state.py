from enum import Enum

class AlertState(Enum):
    white = 0
    """Everything works like a charm"""
    yellow = 1
    """An incident is imminent"""
    red = 2
    """Incident happened"""
    black = 3
    """The state is unknown"""
