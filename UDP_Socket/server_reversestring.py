from socket import *
# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str

s1 = socket(AF_INET,SOCK_DGRAM)
# print(s1),
s1.bind(('172.16.116.147',10002))
# print(s1)
print("Server is Running")
while True:
    Message,Add = s1.recvfrom(1028)
    print(f"Conn:{Add}")
    modi = Message.decode().upper()
    s1.sendto(modi.encode(),Add)
    reversed_string = modi[::-1]
    s1.sendto(reversed_string.encode(),Add)

    s1.close()