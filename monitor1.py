from time import sleep

import zmq
import sys

from zmq.utils.strtypes import unicode


class monitor:
    def __init__(self, type):
        self.socket = None
        self.type = type

    def socket_config(self, type):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:2001')
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")

    def open(self,type):
        self.socket_config(type)
        while True:
            sleep(1)
            publisher_id, self.type, value = self.socket.recv_pyobj()
            print(f"server_{publisher_id} {self.type} {value}")


if __name__ == "__main__":
    monitor1 = monitor(sys.argv[1])
    monitor1.open(type)
