import zmq
import time

class ServerBonus(object):
    """description of class"""

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:18475")
        while True:
            print "Server Bonus is active..."
            request = socket.recv()
            response = self.calculate(request)
            print "received message {0}".format(request)
            socket.send(str(response))

    def calculate(self, request):
        clientid, argumentA, argumentB = request.split(',')
        return "{0}, result:{1}".format(clientid, int(argumentA) * int(argumentB))

if __name__ == "__main__":
    server = ServerBonus()
    server.run()