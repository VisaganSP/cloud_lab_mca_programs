import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send_json({"a": 5, "b": 3})
result = socket.recv_json()
print(f"Result: {result['result']}")
