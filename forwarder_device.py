import zmq


if __name__ == "__main__":
    try:
        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.SUB)
        frontend.bind("tcp://*:2000")

        frontend.setsockopt_string(zmq.SUBSCRIBE, "")

        # Socket facing services
        backend = context.socket(zmq.PUB)
        backend.bind("tcp://*:2001")

        # Creating device
        zmq.device(zmq.FORWARDER, frontend, backend)
    except Exception as e:
        print(e)
        print("Desconectando el dispositivo zqm...")
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()