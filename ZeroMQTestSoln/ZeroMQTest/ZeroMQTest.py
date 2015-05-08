import zmq

context = zmq.Context()
print "Server is about to start..."
socket = context.socket(zmq.REP)
socket.bind("tcp://*.12345")
while True:
    request = socket.recv()
    print request
