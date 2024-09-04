from socket import *

server_socket=socket(AF_INET, SOCK_DGRAM)
print(server_socket)
server_socket.bind(('192.168.191.124',10001))
print(server_socket)

# server_socket.listen(3)
print('Waiting for Connection.....')

while True:

    msg,c_addr=server_socket.recvfrom(1048)
    mod_msg=msg.decode().upper()
    server_socket.sendto(mod_msg.encode(),c_addr)
    server_socket.close()