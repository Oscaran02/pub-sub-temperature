from werkzeug.security import check_password_hash
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
            self.passwords.append(password)

    # Check if the username and password are correct
    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        # Check if the username and password are correct
        if username in self.usernames and check_password_hash(self.passwords[self.usernames.index(username)], password):
            self.login_status = True
        else:
            self.login_status = False

    # Socket configuration
    def socket_config(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:6501')
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")

    # Open the socket
    def open(self):
        self.socket_config()
        while True:
            string = self.socket.recv()
            type, server_id, value, time = string.split()
            server_id = server_id.decode("utf-8")
            type = type.decode("utf-8")
            value = value.decode("utf-8")
            time = time.decode("utf-8")
            print(f"{time}: [server_id:{server_id} type:{type} value:{value}]")


if __name__ == "__main__":
    calidad = calidad()
    # Login
    while not calidad.login_status:
        calidad.login()
    # Open the socket
    calidad.open()
