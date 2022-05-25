import zmq

if __name__ == "__main__":
    try:
        print("Conectando dispositivo zqm de calidad...")

        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.SUB)
        frontend.bind("tcp://*:6500")

        frontend.setsockopt_string(zmq.SUBSCRIBE, "")

        # Socket facing services
        backend = context.socket(zmq.PUB)
        backend.bind("tcp://*:6501")

        # Creating device
        zmq.device(zmq.FORWARDER, frontend, backend)

        print("Dispositivo conectado")

    except Exception as e:
        print(e)
        print("Desconectando el dispositivo zqm de calidad...")
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()