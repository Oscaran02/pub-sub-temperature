from werkzeug.security import check_password_hash
import datetime
import os
import psutil

import zmq


# Sistema de calidad
class calidad:
    def __init__(self):
        self.socket = None
        self.usernames = []
        self.passwords = []
        self.get_users_data()
        self.login_status = False

    # Get the username and password from the file
    def get_users_data(self):
        with open("users.txt") as f:
            contents = f.readlines()
        for line in contents:
            username, password = line.split("::")
            self.usernames.append(username)
            self.passwords.append(password.rstrip())

    # Check if the username and password are correct
    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        # Check if the username and password are correct
        if username in self.usernames and check_password_hash(self.passwords[self.usernames.index(username)], password):
            self.login_status = True
            print("Login successful")
        else:
            print("Incorrect username or password")
            self.login_status = False

    # Socket configuration
    def socket_config(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:6501')
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")

    # Obtiene el tiempo de la operación en segundos decimales
    @staticmethod
    def calculate_operation_time(time):
        timex = datetime.datetime.strptime(time, "%H:%M:%S")
        operation_time = datetime.datetime.now() - timex
        operation_time = operation_time.seconds + operation_time.microseconds / 1000000
        return operation_time

    # Open the socket
    def open(self):
        self.socket_config()
        print("Waiting for data...")
        while True:
            string = self.socket.recv()  # Receive the data
            server_id, type, value, time, time_monitor = string.split()  # Split the data
            server_id = server_id.decode("utf-8")
            type = type.decode("utf-8")
            value = value.decode("utf-8")
            time = time.decode("utf-8")
            time_monitor = time_monitor.decode("utf-8")
            time_monitor = self.calculate_operation_time(time_monitor)  # Calculate the operation time
            # Print the data
            print(
                f"{time}: [server_id:{server_id} type:{type} value:{value}] (tiempo de la operación: {time_monitor}s)")

            print(f'\t\tRAM memory % available: {100 - psutil.virtual_memory()[2]}%')


if __name__ == "__main__":
    calidad = calidad()
    # Login
    while not calidad.login_status:
        calidad.login()
    # Open the socket
    calidad.open()
