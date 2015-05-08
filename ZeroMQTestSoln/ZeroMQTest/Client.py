import zmq

class Client:
    """description of class"""
    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:12345")
        while True:
            socket.send(b"data")
            print "message send..."
            response = socket.recv()
            print "...and received";


if __name__ == "__main__":
    client = Client()
    client.run()