from abc import ABCMeta, abstractmethod
from alert import Alert


class Informer(metaclass=ABCMeta):
    """An informer class is responsible to inform the server adminstrator.

    This may fulfilled by sending SMS messages, emails or any other convenient
    way.
    """
    @abstractmethod
    def inform(self, alert: Alert) -> bool:
        """This have to be implemented by a subclass to send alerts to the
        administrator.

        This method is called by the program's main loop each time a watcher
        find something bad.

        Args:
            alert: the alert sent by a watcher."""
        pass
