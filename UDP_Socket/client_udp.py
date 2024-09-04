from socket import *

client_socket=socket(AF_INET,SOCK_DGRAM)

msg=input('Input message in lower case:')
client_socket.sendto(msg.encode(),('192.168.191.124',10001))
mod_msg,server_addr=client_socket.recvfrom(1048)
print(mod_msg.decode())
client_socket.close()



