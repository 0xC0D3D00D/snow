from alert_state import AlertState
from time import sleep


class Snow:
    def __init__(self):
        self.watchmen = []
        self.informers = []

    def register_watchman(self, watchman):
        if watchman not in self.watchmen:
            self.watchmen.append(watchman)

    def register_informer(self, informer):
        if informer not in self.informers:
            self.informers.append(informer)

    def iterate_once(self):
        for watchman in self.watchmen:
            if watchman.outpost() != AlertState.white:
                for informer in self.informers:
                    informer.inform(watchman.get_last_alert())

    def iterate(self, interval):
        while True:
            self.iterate_once()
            sleep(interval)
