import zmq
from time import sleep
import sys

class sensor:
    def __init__(self, type, time, conf):
        self.type = type
        self.time = time
        self.conf = conf


    def socket_settings(self):
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind('tcp://127.0.0.1:2000')
        return socket




messages = [100, 200, 300]
current_message = 0

while True:
    sleep(1)
    socket.send_pyobj(1+current_message)

    if current_message == 2:
        current_message = 0
    else:
        current_message = current_message+1

if __name__ == '__main__':
