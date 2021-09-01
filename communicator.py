class Communicator:
    def __init__(self):
        self.observers = list()

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def broadcast(self, message):
        for observer in self.observers:
            observer.notify(message)
