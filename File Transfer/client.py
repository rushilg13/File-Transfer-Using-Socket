import socket

s = socket.socket()
host = input("Enter host name of sender: ")
port = 8080
s.connect((host, port))
print("Connected")

filename = input("Please Enter filename or incoming file: ")
file = open(filename, "wb")
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully!")