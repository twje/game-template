class Message:
    def __init__(self, msg_id, payload=None):
        self.msg_id = msg_id
        self.payload = payload
        self.response = None
