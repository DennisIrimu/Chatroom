from channels import include

# Display messages in the console
def message_handler(message):
    print(message['text'])

# Register message handler
channel_routing = [
    include("chat.routing.websocket_routing",path=r"^/chat/stream"),
    include("chat.routing.custom_routing"),
]
