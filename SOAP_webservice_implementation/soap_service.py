from spyne import Application, rpc, ServiceBase, Integer, Unicode, AnyDict
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.complex import Iterable

# In-memory store for items (simulates a database)
items = {
    1: {"name": "Item1", "description": "First item"},
    2: {"name": "Item2", "description": "Second item"}
}

# Define the SOAP service
class ItemService(ServiceBase):

    @rpc(_returns=Iterable(AnyDict))
    def GetItems(ctx):
        """Simulates GET request - Returns all items."""
        return [item for item in items.values()]

    @rpc(Integer, _returns=AnyDict)
    def GetItem(ctx, id):
        """Simulates GET request - Returns an item by ID."""
        return items.get(id, {"error": "Item not found"})

    @rpc(Unicode, Unicode, _returns=Unicode)
    def CreateItem(ctx, name, description):
        """Simulates POST request - Creates a new item."""
        new_id = max(items.keys()) + 1
        items[new_id] = {"name": name, "description": description}
        return f"Item {new_id} created."

    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def UpdateItem(ctx, id, name, description):
        """Simulates PUT request - Updates an existing item."""
        if id in items:
            items[id] = {"name": name, "description": description}
            return f"Item {id} updated."
        return "Item not found."

    @rpc(Integer, Unicode, _returns=Unicode)
    def PatchItem(ctx, id, description):
        """Simulates PATCH request - Partially updates an item."""
        if id in items:
            items[id]["description"] = description
            return f"Item {id} description updated."
        return "Item not found."

    @rpc(Integer, _returns=Unicode)
    def DeleteItem(ctx, id):
        """Simulates DELETE request - Deletes an item."""
        if id in items:
            del items[id]
            return f"Item {id} deleted."
        return "Item not found."

# Spyne application definition
application = Application(
    [ItemService],  # List of services
    tns="http://example.com/soap-service",  # Target namespace
    in_protocol=Soap11(validator='lxml'),   # Input protocol (SOAP 1.1)
    out_protocol=Soap11()                   # Output protocol (SOAP 1.1)
)

# WSGI Application to host the SOAP service
wsgi_application = WsgiApplication(application)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    print("SOAP service running on http://127.0.0.1:8000/soap-service")
    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
