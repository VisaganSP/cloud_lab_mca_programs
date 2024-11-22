import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://localhost:9000/")
result = client.add(20, 10)
print(f"Result: {result}")
