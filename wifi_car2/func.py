# -*- coding: utf-8 -*-
import pygame
import time
import socket
import Queue
import re
import threading

c_queue= Queue.Queue(2)     # kolejka  do trzymania znalezionego IP - odporna na wiele w�tk�w 

# funkcja do wysetlania warotsci 
def print_value (screen, text, _font, font_size, color, _x, _y):
    my_font_value = pygame.font.SysFont(_font, font_size)
    screen.blit( my_font_value.render(text,1,color)     ,( _x, _y))
    
# pozbywa sie wartosci po ostatniej kropce  w adresie IP
def extractIP( ipStr):
    l = re.split('(.*)\.(.*)\.(.*)\.(.*)', ipStr)
    print str(l[1]+"."+l[2]+"."+l[3]+".")
    return str(l[1]+"."+l[2]+"."+l[3]+".")

# funkcja szukajaca adresu IP ( z danego zakresu )  z otwartym portem 
def find_server (start, stop, host, port ):
    full_host = ""
    c_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #print "zasieg: " + str(start) + " " + str(stop)
    for x in range(start,stop):
        full_host = host + str(x)
        if c_queue.empty() == False:     # jesli cos jest w kolejce oznacza ze adres zostal odnaleziony wiec inne watki nie musza juz szukac 
            break
        # sprawdza czy moze sie polaczyc   jesli nie zwraca wyjatek   ktory lapiemy  i przechodzimy do kolejnego adresu  z  podanego zakresu 
        try:
            c_socket.connect((full_host,port))
        except socket.error, msg : 
            #print full_host+" " + str( msg[0]) +" "+ unicode(msg[1], "windows-1250")
            continue
        else:
            if c_queue.empty() == True:
                c_queue.put(full_host)
            #print "OK - HOST: "+full_host
            return "OK - HOST: "+full_host
    print "KONIEC!!: " + str(start) + " " + str(stop)
    return "NOT FOUND" 
# funkcja   watek 
def find_ip_start (port):
    # pobiera adres kienta   ( dzieki temu znamy adres sieci w jakiej pracuje klient i szukany serwer)
    adres = extractIP(str(socket.gethostbyname(socket.gethostname())))   
    c_thread = [0]   
    # przeszukujemy koncwke  adresow z sieci  ( bo jest mniejsza niz 10   - nie ma 260   tylko 255 )
    c_thread[0] = threading.Thread(target = find_server , args = (251,255,adres, port ))
    c_thread[0].start() 
    # tworzymy nowe watki  (25 sztuk )  ktore przeszukuja zakresy adresow 
    for num in range(1, 26):
        c_thread.extend("0")   # poszerzamy liste watkow 
        c_thread[num] = threading.Thread(target = find_server , args = ((num-1)*10+1,num*10,adres, port ))
        c_thread[num].start()
        