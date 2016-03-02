from watchman import Watchman
from alert import Alert
from alert_state import AlertState
import psutil
import humanize

stat_tmpl = """
Memory stats
===================
Available: {available}
Free: {free}
Used: {used}
Total: {total}
Active: {active}
Inactive: {inactive}
Buffers: {buffers}
Cached: {cached}
"""


class MemoryWatch(Watchman):
    def __init__(self, config):
        super(MemoryWatch, self).__init__(config)
        self.last_alert = None

    def outpost(self):
        memory_values = psutil.virtual_memory()
        total = memory_values.total
        available = memory_values.available
        used = memory_values.used
        free = memory_values.free
        active = memory_values.active
        inactive = memory_values.inactive
        buffers = memory_values.buffers
        cached = memory_values.cached

        mem_stats = stat_tmpl.format(available=humanize.naturalsize(available),
                                     free=humanize.naturalsize(free),
                                     used=humanize.naturalsize(used),
                                     total=humanize.naturalsize(total),
                                     active=humanize.naturalsize(active),
                                     inactive=humanize.naturalsize(inactive),
                                     buffers=humanize.naturalsize(buffers),
                                     cached=humanize.naturalsize(cached))

        self.last_alert = Alert()
        self.last_alert.set_watcher_name(self.__class__.__name__)
        if free/total <= float(self.config["free_red_threshold"]):
            alert_message = "Free memory is in emeregency level!\n" + \
                            mem_stats
            self.last_alert.set_message(alert_message)
            self.last_alert.set_state(AlertState.red)
        elif available/total <= float(self.config["available_red_threshold"]):
            alert_message = "Available memory is in emeregency level!\n" + \
                            mem_stats
            self.last_alert.set_message(alert_message)
            self.last_alert.set_state(AlertState.red)
        elif free/total <= float(self.config["free_yellow_threshold"]):
            alert_message = "Free memory is in critical level\n" + mem_stats
            self.last_alert.set_message(alert_message)
            self.last_alert.set_state(AlertState.yellow)
        elif available/total <= float(self.config["available_yellow_threshold"]):
            alert_message = "Available memory is in critical level\n" + mem_stats
            self.last_alert.set_message(alert_message)
            self.last_alert.set_state(AlertState.yellow)
        else:
            return AlertState.white

        return self.last_alert.get_state()

    def get_last_alert(self):
        return self.last_alert
