from informer import Informer
import telegram


class TelegramInformer(Informer):
    def __init__(self, config):
        self.bot = telegram.Bot(config["token"])
        self.chats = []
        for u in self.bot.getUpdates():
            if u.message.text == '/auth gx34idjnoe':
                print(u.to_json())
                self.chats.append(u.message.chat_id)

    def inform(self, alert):
        for chat_id in self.chats:
            self.bot.sendMessage(chat_id=chat_id, text=alert.__str__())
