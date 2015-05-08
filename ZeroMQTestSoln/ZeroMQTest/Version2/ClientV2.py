import zmq
import time

class ClientV2(object):
    """description of class"""

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:18475")
        while True:
            print "Client version 2 is active..."
            socket.send("5,4")
            response = socket.recv()
            print "Response is {0}".format(response)
            time.sleep(2)

if __name__ == "__main__":
    client = ClientV2()
    client.run()