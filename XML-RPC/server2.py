import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_json()
    result = message["a"] + message["b"]
    socket.send_json({"result": result})
