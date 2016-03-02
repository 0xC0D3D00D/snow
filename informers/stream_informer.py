from informer import Informer

class StreamInformer(Informer):
    def inform(self, alert):
        print(alert)
