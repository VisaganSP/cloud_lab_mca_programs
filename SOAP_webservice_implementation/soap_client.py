from zeep import Client

# URL to the WSDL
wsdl_url = 'http://127.0.0.1:8000/soap-service?wsdl'

# Create a Zeep client using the WSDL
client = Client(wsdl=wsdl_url)


def extract_item_data(item):
    """Extracts item data from the Element objects."""
    return {
        "name": item[0].text,
        "description": item[1].text
    }


# 1. Get all items (GET equivalent)
items = client.service.GetItems()
print("All Items:", [extract_item_data(item) for item in items])

# 2. Get a single item by ID (GET equivalent)
item = client.service.GetItem(1)
print("Item 1:", extract_item_data(item))

# 3. Create a new item (POST equivalent)
response = client.service.CreateItem("NewItem", "This is a new item.")
print("Create Item Response:", response)

# 4. Update an existing item (PUT equivalent)
response = client.service.UpdateItem(
    2, "UpdatedItem2", "Updated description for item 2.")
print("Update Item Response:", response)

# 5. Partially update an item (PATCH equivalent)
response = client.service.PatchItem(1, "Updated description for item 1.")
print("Patch Item Response:", response)

# 6. Delete an item by ID (DELETE equivalent)
response = client.service.DeleteItem(2)
print("Delete Item Response:", response)

# Check remaining items after deletion
items = client.service.GetItems()
print("Items after deletion:", [extract_item_data(item) for item in items])
