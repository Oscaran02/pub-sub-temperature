import zmq


class monitor:
    def __init__(self):
        self.socket = None

    def socket_config(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:5501')
        topic_filter = "temperatura"  # 1 ph, 2 temperatura y 3 oxigeno
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

    def open(self):
        self.socket_config()
        while True:
            string = self.socket.recv()
            topic, server_id, type, value = string.split()
            server_id = server_id.decode("utf-8")
            type = type.decode("utf-8")
            value = value.decode("utf-8")
            print(f"[server_id:{server_id} type:{type} value:{value}]")


if __name__ == "__main__":
    monitor1 = monitor()
    monitor1.open()
