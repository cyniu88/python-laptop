import pygame
from pygame.locals import *
import sys
import os
import socket
import time
import func
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

pygame.init()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
message = " "
tm ="NULL"
tmpSTR = ""
axies_now = [0,0,0,0]
button_now = [0,0,0,0,0,0,0,0,0,0,0,0]
hats_now = (0,0)
my_ping = 0
my_siz = (1200,800)
my_siz_org = (1200,800)
my_x_plus = 410
my_y_plus = 410
my_x = my_siz_org[0] - my_x_plus
my_y = my_siz_org[1] - my_y_plus

my_rel = (0,0)

my_font_title = pygame.font.SysFont("Arial", 28,1,1)

my_title = 'WiFi Robot control  ver1.0'
my_title_render = my_font_title.render(my_title,1, WHITE)
 
# utworzenie okna
window = pygame.display.set_mode(my_siz_org,HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.mouse.set_visible(1)
pygame.event.set_grab(0)

window.fill(BLACK)
my_art_BG = pygame.image.load('background2.png')
# ustawiamy etykiete
pygame.display.set_caption(my_title)
# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()

#  Start connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
if len(sys.argv) >= 3 :
    host = sys.argv[1]
    port = int(sys.argv[2])
    #print("podales dobre argumenty")
else:
    print("adres i port domyslny ")
    host = "192.168.1.144"
    port = int(8833)
# connection to hostname on the port.
s.connect((host, port))
# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        elif event.type==VIDEORESIZE:
            my_siz =event.dict['size']
            windows=pygame.display.set_mode(my_siz,HWSURFACE|DOUBLEBUF|RESIZABLE)


            my_x = my_siz[0] - my_x_plus
            my_y = my_siz[1] - my_y_plus

            print (my_x)
            print (my_y)
            #time.sleep(10)

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    #print ( "Number of joysticks: %i" %joystick_count)
    window.fill(BLACK)

    if not pygame.mouse.get_pressed()[0]:
        hendle = False
    if  pygame.mouse.get_pressed()[0]:
        if   pygame.mouse.get_pos()[0] > my_x and pygame.mouse.get_pos()[0] < my_x + 400 and  pygame.mouse.get_pos()[1] > my_y and   pygame.mouse.get_pos()[1] < my_y +390 :
            hendle = True

        if hendle == True :
            my_rel = pygame.mouse.get_rel()
            my_x = my_x + my_rel[0]
            my_x_plus -= my_rel[0]
            my_y = my_y + my_rel[1]
            my_y_plus -= my_rel[1]
    screen.blit(my_art_BG, (my_x,my_y))



    if int(button_now[10]) == 1 :
        pygame.draw.circle(window, RED, ((int(axies_now[0]) )/10 +my_x+145,(int(axies_now[1]) )/10+my_y+310), 25, 0)
    else:
        pygame.draw.circle(window, GREEN, ((int(axies_now[0]) )/10 +my_x+145,(int(axies_now[1]) )/10+my_y+310), 25, 0)
     
    
    func.print_value(screen ,str(axies_now[0]), "Impact", 12, BLUE, (int(axies_now[0]) )/10 +my_x+136, (int(axies_now[1]) )/10+my_y+310)
    func.print_value(screen ,str(axies_now[1]), "Impact", 12, BLUE, (int(axies_now[0]) )/10 +my_x+140, (int(axies_now[1]) )/10+my_y+290)
    if int(button_now[11]) == 1 :
        #pygame.draw.circle(window, RED, (  (int(axies_now[2]) )/10+my_x+462, (int(axies_now[3]) )/10+my_y+320), 25, 0)
        pygame.draw.circle(window, RED, (  (int(axies_now[2]) )/10+my_x+268, (int(axies_now[3]) )/10+my_y+311), 25, 0)
    else:
        pygame.draw.circle(window, GREEN, (  (int(axies_now[2]) )/10+my_x+268, (int(axies_now[3]) )/10+my_y+311), 25, 0)
        
    func.print_value(screen ,str(axies_now[2]), "Impact", 12, BLUE, (int(axies_now[2]) )/10 +my_x+262, (int(axies_now[3]) )/10+my_y+311)
    func.print_value(screen ,str(axies_now[3]), "Impact", 12, BLUE, (int(axies_now[2]) )/10 +my_x+266, (int(axies_now[3]) )/10+my_y+291)
    # butons 
    
    if int(button_now[0]) == 1 :     #       522 - 205      232 -10
        pygame.draw.circle(window, RED, (   my_x+327, my_y+222), 15, 0)
    if int(button_now[1]) == 1 :
        pygame.draw.circle(window, RED, (   my_x+359, my_y+252), 15, 0)
    if int(button_now[2]) == 1 :
        pygame.draw.circle(window, RED, (   my_x+326, my_y+282), 15, 0)
    if int(button_now[3]) == 1 :
        pygame.draw.circle(window, RED, (   my_x+290, my_y+252), 15, 0)
    if int(button_now[4]) == 1 :
        pygame.draw.rect(window, RED, (55+my_x, 75+my_y, 50 , 30))
    if int(button_now[5]) == 1 :
        pygame.draw.rect(window, RED, (308+my_x, 75+my_y, 50 , 30))
    if int(button_now[6]) == 1 :
        pygame.draw.rect(window, RED, (59+my_x, 20+my_y, 50 , 40))
    if int(button_now[7]) == 1 :
        pygame.draw.rect(window, RED, (310+my_x, 22+my_y, 50 , 40))
    if int(button_now[8]) == 1 :
        pygame.draw.rect(window, RED, (165+my_x, 246+my_y, 15 , 10))
    if int(button_now[9]) == 1 :
        pygame.draw.rect(window, RED, (231+my_x, 246+my_y, 15 , 10))
    if hats_now[0]== -1:
        pygame.draw.rect(window, RED, (55+my_x, 242+my_y, 20 , 20))
    if hats_now[0]== 1:
        pygame.draw.rect(window, RED, (97+my_x, 242+my_y, 20 , 20))
    if hats_now[1]== 1:
        pygame.draw.rect(window, RED, (77+my_x, 222+my_y, 20 , 20))
    if hats_now[1]== -1:
        pygame.draw.rect(window, RED, (77+my_x, 265+my_y, 20 , 20))
         
    screen.blit(my_title_render, (10,10))
    func.print_value(screen, "Message sent:     "+message, "Arial", 14, WHITE, 370,  10)
    func.print_value(screen, "Message received: "+tm, "Arial", 14, WHITE, 370, 28)

    func.print_value(screen, str(pygame.mouse.get_rel()), "Arial", 14, WHITE, my_siz[0] - (my_siz_org[0] - 1000), 50)
    func.print_value(screen, str(pygame.mouse.get_pos()), "Arial", 14, WHITE, my_siz[0] - (my_siz_org[0] - 1000), 65)


    func.print_value(screen, "PING: "+str( my_ping), "Arial", 15, WHITE, my_siz[0] - (my_siz_org[0] - 1000), 80)

    pygame.display.update()
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        message="joy:"+ str(i)+";"
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        #print("Joystick name: %s" %name)

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        #print (  "Number of axes: %i" %axes)
        message +="axes"
        for i in range(axes):
            axis = joystick.get_axis(i)
            message +=":"
            tmpSTR = axies_now[i]= str(int(axis *255.6))
            
            while len(tmpSTR) < 4:
                tmpSTR+=" "
            message += tmpSTR
            #print ("warotsc z axis 0 : %f" %joystick.get_axis(i))
            #print (" ")


        buttons = joystick.get_numbuttons()
        #print ( "Number of buttons: %i "%buttons)

        message+=";button"
        for i in range(buttons):
            button = joystick.get_button(i)
            #print ( "Button %i" %i )
            #print (" value: %s " %button)
            button_now[i]= button
            message+=":"+str(i)+"="+str(button)
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        #print ( "Number of hats: %i" %hats)

        message+=";hats"
        for i in range(hats):
            hat = joystick.get_hat(i)
            #print (  "Hat %i " %i )
            #print (" value: %s " %str(hat))
            hats_now = hat
            message+=":"+str(i)+"="+str(hat)

        message+=";END"
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.


    # Limit to 60 frames per second
    print (message)
    print ("wielkosc %i" %len(message))
    my_ping = int(round(time.time() * 1000))
    s.send (message)
    print(" odbieramy")
    
    tm = s.recv(256)
    my_ping -= int(round(time.time() * 1000))
    my_ping *=-1
    print ("odebrano: ")
    #print(tm)
    clock.tick(30)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()