from xmlrpc.server import SimpleXMLRPCServer


def add(a, b):
    return a + b


with SimpleXMLRPCServer(("localhost", 9000)) as server:
    server.register_function(add, "add")
    print("Server is running...")
    server.serve_forever()
