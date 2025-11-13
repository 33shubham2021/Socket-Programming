import socket

# attributes  = type_of_ip and type_of_transport_layer_protocol
#AF_INET = ipv4    AF = Address Family
#SOCK_STREAM = TCP 

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect(("localhost" , 8080))

# send data in one go..all the chunks/segments
# send only sends one segment at a time, therefore a loop will be required

s.sendall(b"Hello Mate, I am Shubham")

data = s.recv(1024)  # buffer of received data should be max 1024 bytes

print(data)

s.close()

