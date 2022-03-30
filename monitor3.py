from time import sleep

import zmq
import sys


class monitor:
    def __init__(self, type):
        self.socket = None

    def socket_config(self, type):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:5501')
        topicfilter = "3"  # 1 ph, 2 temperatura y 3 oxigeno
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

    def open(self, type):
        self.socket_config(type)
        while True:
            string = self.socket.recv()
            topic, server_id, type, messagedata = string.split()
            print(server_id, type, messagedata)


if __name__ == "__main__":
    monitor1 = monitor(sys.argv[1])
    monitor1.open(type)
