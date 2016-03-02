import configparser
import argparse
from snow import Snow
from watchmen.memory_watch import MemoryWatch
from informers.stream_informer import StreamInformer
from informers.telegram_informer import TelegramInformer


def main():
    parser = argparse.ArgumentParser(description='Snow - for the watch')
    parser.add_argument('--config', dest='config_file', action='store',
                        default='/etc/snow.ini',
                        help='Address to the config file')
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config_file)

    snow = Snow()
    if 'memory_watch' in config:
        snow.register_watchman(MemoryWatch(config['memory_watch']))
    if 'stream_informer' in config:
        snow.register_informer(StreamInformer())
    if 'telegram_informer' in config:
        snow.register_informer(TelegramInformer(config['telegram_informer']))

    snow.iterate(float(config["main"]["check_interval"]))

if __name__ == "__main__":
    main()
