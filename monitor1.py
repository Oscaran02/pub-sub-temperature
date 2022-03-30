import zmq
import sys


class monitor:
    def __init__(self, type):
        self.socket = None
        self.type = type

    def socket_config(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:2001')
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self.type)

    def open(self):
        while True:
            message = self.socket.recv_pyobj()
            print(message)



if __name__ == "__main__":
    monitor1 = monitor(sys.argv[1])
