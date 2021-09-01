from collections import defaultdict
from communicator import Communicator


class MessageHandler:
    def __init__(self) -> None:
        self.subscriptions = defaultdict(Communicator)

    def subscribe(self, msg_id, observer):
        self.subscriptions[msg_id].subscribe(observer)

    def unsubscribe(self, msg_id, observer):
        self.subscriptions[msg_id].unsubscribe(observer)

    def dispatch(self, message):
        self.subscriptions[message.msg_id].broadcast(message)
