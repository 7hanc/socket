
import socket

def client():
    host = socket.gethostname()  
    port = 5000 
    
    client_socket = socket.socket()  
    client_socket.connect((host, port))  
    
    message = input(" -> ") 
    while message!='bye':
         
        client_socket.send(message.encode())     # send message to server
        server_time = client_socket.recv(1024)   # read at most 1024 bytes
        str_length =  client_socket.recv(1024)
     
        print ('Time of server:', server_time)
        print('Length of string:', str_length)
        message = input(" -> ") 
        
    client_socket.close()  
    
client()
