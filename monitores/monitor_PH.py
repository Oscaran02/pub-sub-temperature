import zmq
import datetime
import os

cwd = os.getcwd()  # Get the current working directory (cwd)


class monitor:
    def __init__(self):
        self.socket = None
        self.socket_pub = None

    # Configuration del socket para escuchar
    def socket_config(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect('tcp://127.0.0.1:5501')
        topic_filter = "PH"  # 1 ph, 2 temperatura y 3 oxigeno
        self.socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

    # Configuration del socket para publicar
    def socket_config_pub(self):
        context = zmq.Context()
        self.socket_pub = context.socket(zmq.PUB)
        self.socket_pub.connect('tcp://127.0.0.1:6500')  # Connecting to the forwarder device

    # Obtiene el tiempo de la operación en segundos decimales
    @staticmethod
    def calculate_operation_time(time):
        timex = datetime.datetime.strptime(time, "%H:%M:%S")
        operation_time = datetime.datetime.now() - timex
        operation_time = operation_time.seconds + operation_time.microseconds / 1000000
        return operation_time

    # Guardar el valor en un archivo
    def save_value(self, type, server_id, value, time):
        with open(f"{cwd}/historial_sensores/{type}.txt", "a", encoding="UTF-8") as file:
            file.write(f"{time}: {value} {server_id} (tiempo de la operación: {self.calculate_operation_time(time)}s\n")

    # Abrir la función del monitor
    def open(self):
        self.socket_config()
        self.socket_config_pub()
        while True:
            string = self.socket.recv()
            type, server_id, value, time = string.split()
            server_id = server_id.decode("utf-8")
            type = type.decode("utf-8")
            value = value.decode("utf-8")
            time = time.decode("utf-8")

            value = float(value)
            if value < 0:  # If the value is negative, it is not a valid value
                pass
            elif 6.0 <= value <= 8.0:  # If the value is a valid value
                self.save_value(type, server_id, value, time)
            else:  # If the value is out of range
                self.save_value(type, server_id, value, time)
                time_monitor = datetime.datetime.now().strftime("%H:%M:%S")
                # Alarma al sistema de calidad
                self.socket_pub.send_string(f"{server_id} {type} {value} {time} {time_monitor}")


if __name__ == "__main__":
    monitor1 = monitor()
    monitor1.open()
