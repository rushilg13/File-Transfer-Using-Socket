import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print("Waiting for connections...")
conn, addr = s.accept()
print(addr, "Has connected to the server")

filename = input("Please enter filename of the file: ")
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("data has been transmitted Successfully")