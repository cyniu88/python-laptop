import socket
import time
import sys

import pygame.camera
import pygame.image


pygame.camera.init()

cameras = pygame.camera.list_cameras()

print "Using camera %s ..." % cameras[0]

webcam = pygame.camera.Camera(cameras[0])

webcam.start()

# grab first frame
img = webcam.get_image()

WIDTH = img.get_width()
HEIGHT = img.get_height()
screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
pygame.display.set_caption("pyGame Camera View")




UDP_IP = "127.0.0.1"
UDP_PORT = 8834
work = True
max_size_pocket = 64000
while True:
        work = True
        sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        sock.bind((UDP_IP, UDP_PORT))
        msg=" "
        while work:
                for e in pygame.event.get() :
                        
                        if e.type == pygame.QUIT :
                             sys.exit()
                
                # draw frame

                # grab next frame
                
                img = webcam.get_image()
                screen.blit(img, (0,0))
                pygame.display.flip()
                pygame.image.save(img, "image.jpg")
                _file = open('image.jpg','rb')
                fp = _file.read()
                _file.close()
                #print fp
                foto_len = len(fp)
                foto_len_tmp = 0 #foto_len
                print "dlugosc to : ",foto_len
                while work:
        
                        data, addr = sock.recvfrom(max_size_pocket) # buffer size is 1024 bytes
                        if data == "END#":
                                 work = False
                                 break
                        print "received message:", data," from: " , addr
                        #time.sleep(1)
                        #print " loop"
                        if foto_len_tmp+max_size_pocket < foto_len:
                                 #print "wysylam zawartosc",foto_len_tmp, " ", foto_len_tmp+max_size_pocket
                                 sock.sendto(fp[foto_len_tmp:foto_len_tmp+max_size_pocket], addr)
                                 foto_len_tmp = foto_len_tmp + max_size_pocket
                                #print "wysylam zawartosc"
                        else :
                                 sock.sendto(fp[foto_len_tmp:foto_len], addr)
                                 print " ostatnia paczka"
                                 break
                data, addr = sock.recvfrom(max_size_pocket) # buffer size is 1024 bytes
                sock.sendto("END#", addr)
                #print "wyslalem"
