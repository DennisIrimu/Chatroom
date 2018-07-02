from channels import route

# Display messages in the console
def message_handler(message):
    print(message['text'])

# Register message handler
channel_routing = [
    route("websocket.receive",message_handler)
]
