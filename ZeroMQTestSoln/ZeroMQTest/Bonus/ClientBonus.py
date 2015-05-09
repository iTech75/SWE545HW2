import zmq
import time
import random

class ClientBonus:
    """description of class"""

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:18475")
        clientid = random.randint(100, 999)
        print "client id: {0}".format(clientid)
        print "Client Bonus is active..."
        while True:
            x = random.randint(1,10)
            y = random.randint(1,10)
            request = "{0},{1},{2}".format(clientid, x, y)
            socket.send(request)
            print "Request sent: {0}".format(request)
            response = socket.recv()
            print "Response is {0}".format(response)
            time.sleep(1)

if __name__ == "__main__":
    client = ClientBonus()
    client.run()