import socket

# Get all network interfaces
interfaces = socket.if_nameindex()

for index, name in interfaces:
    print(f"Interface {index}: {name}")
