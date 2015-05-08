import zmq
import time

class ServerV1(object):
    """description of class"""

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:18475")
        while True:
            print "Server version 1 is active..."
            request = socket.recv()
            print "received message {0}".format(request)
            socket.send(request)

if __name__ == "__main__":
    server = ServerV1()
    server.run()