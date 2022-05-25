import zmq

if __name__ == "__main__":
    try:
        print("Conectando dispositivo zqm...")
        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.SUB)
        frontend.bind("tcp://*:5500")

        frontend.setsockopt_string(zmq.SUBSCRIBE, "")

        # Socket facing services
        backend = context.socket(zmq.PUB)
        backend.bind("tcp://*:5501")

        print("Dispositivo conectado")
        # Creating device
        zmq.device(zmq.FORWARDER, frontend, backend)
    except Exception as e:
        print(e)
        print("Desconectando el dispositivo zqm...")
    finally:
        frontend.close()
        backend.close()
        context.term()