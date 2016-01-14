import socket
import time
from _socket import SHUT_RDWR
class c_connect :
    c_socket = 0
    work = False
    def __init__(self):
        print "tworze obiekt do polaczenia"
    def is_work(self):
        return self.work    
     
    def __del__(self):
        print "obiekt niszczony"
        
    def send (self,c_msg):
        if self.work == True:
            return self.c_socket.send(c_msg)
        else:
            return 0
    def recv (self,size):
        if self.work == True:
            return self.c_socket.recv(size)
        else:
            return "NULL"
    def connect_to (self,host, port):
        self.c_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.c_socket.connect((host,port)) 
        except socket.error, msg:
            print msg
            self.work = False
            return msg
        self.work=True
        return "OK - HOST: "+host
    def disconnect_now (self):
        print "disconnect"
        self.send("DISCONNECT#")
        self.c_socket.shutdown(SHUT_RDWR)
        self.work = False
        return "DISCONNECTED"

    