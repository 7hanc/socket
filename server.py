import socket
from time import ctime

def server():
   
    host = socket.gethostname()
    port = 5000 
    server_socket = socket.socket()  
    
    server_socket.bind((host, port)) 
   
    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
       
        data = conn.recv(1024).decode()  #read at most 1024 bytes
        if not data:
            break
            
        print("From client: " + str(data))
        data_length = len(data)
        
        server_time = ctime()   #get server's time
        conn.sendall(server_time.encode())  #encode():convert to bytes
        conn.sendall(str(data_length).encode())

    conn.close()  
    
server()
