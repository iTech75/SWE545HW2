import zmq
import time

class ServerV2(object):
    """description of class"""

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:18475")
        while True:
            print "Server version 2 is active..."
            request = socket.recv()
            response = self.calculate(request)
            print "received message {0}".format(request)
            socket.send(str(response))

    def calculate(self, request):
        argumentA, argumentB = request.split(',')
        return int(argumentA) * int(argumentB)

if __name__ == "__main__":
    server = ServerV2()
    server.run()