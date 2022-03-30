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
        self.socket = None

    # To make the socket settings
    def socket_config(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.PUB)
        self.socket.connect('tcp://127.0.0.1:5500') # Connecting to the forwarder device

    # Used in function make values
    def conf_values(self):
        with open(self.conf) as f:
            contents = f.readlines()
        self.correct_values = float(contents[0])
        self.out_of_range_values = float(contents[1])
        self.error_values = float(contents[2])

    # Used to make the values according to the configuration defined
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
                    yield random.randint(0, local_range[0])  # Number below the range
                else:
                    yield random.randint(local_range[1], 100)  # Number above the range
            else:  # bad values
                yield -1

    # Used to open the sensor
    def open(self):
        self.socket_config()
        value = self.make_values()
        publisher_id = random.randrange(0, 9999)
        while True:
            sleep(self.time)
            if self.type == "PH":
                self.socket.send_string(("%d %d %s %d" % (1, publisher_id, self.type, next(value))))
            elif self.type == "temperatura":
                self.socket.send_string(("%d %d %s %d" % (2, publisher_id, self.type, next(value))))
            elif self.type == "oxigeno":
                self.socket.send_string(("%d %d %s %d" % (3, publisher_id, self.type, next(value))))


if __name__ == '__main__':
    sensor1 = sensor(sys.argv[1], sys.argv[2], sys.argv[3])
    sensor1.open()
