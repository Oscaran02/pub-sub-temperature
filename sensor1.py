import zmq
from time import sleep
import sys
import random


class sensor:
    def __init__(self, type, time, conf):
        self.type = type
        self.time = int(time)
        self.conf = conf
        self.correct_values = None
        self.out_of_range_values = None
        self.error_values = None

    # To make the socket settings
    @staticmethod
    def socket_settings():
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind('tcp://127.0.0.1:2000')
        return socket

    # Used in function make values
    def conf_values(self):
        with open(self.conf) as f:
            contents = f.readlines()
        self.correct_values = contents[0]
        self.out_of_range_values = contents[1]
        self.error_values = contents[2]

    def make_values(self):
        self.conf_values()
        if self.type == "PH":
            local_range = [6, 8]
        elif self.type == "temperatura":
            local_range = [68, 89]
        else:
            local_range = [2, 11]
        while True:
            random_number = random.random()
            if random_number < self.correct_values:  # Correct values
                yield random.randint(local_range[0], local_range[1])
            elif random_number < self.correct_values + self.out_of_range_values:  # Out of range values
                if random.random() < 0.5:
                    random.randint(0, local_range[0])
                else:
                    random.randint(local_range[1], 100)
            else:  # bad values
                yield -1

    def open(self):
        messages = [100, 200, 300]
        current_message = 0

        while True:
            sleep(self.time)
            self.socket.send_pyobj(1 + current_message)

            if current_message == 2:
                current_message = 0
            else:
                current_message = current_message + 1


if __name__ == '__main__':
    sensor(sys.argv[1], sys.argv[2], sys.argv[3])
