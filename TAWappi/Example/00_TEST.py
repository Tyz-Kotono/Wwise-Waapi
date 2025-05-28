from waapi import WaapiClient

# Connect (default URL)
client = WaapiClient()

# RPC
result = client.call("ak.wwise.core.getInfo")
result = client.call(
    "ak.wwise.ui.getSelectedObjects",
    options={"return": ["id", "type", "name"]},
)
print(result)
# Subscribe
handler = client.subscribe(
    "ak.wwise.core.object.created",
    lambda object: print("Object created: " + str(object)),
)


# Bind a different callback at any time
def my_callback(object):
    print("Different callback: " + str(object))


handler.bind(my_callback)

# Unsubscribe
handler.unsubscribe()

# Disconnect
client.disconnect()
