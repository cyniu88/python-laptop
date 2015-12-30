
import pygame
import sys
import socket
import time
from sys import stdout

pygame.init()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
message = " "

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
    port = int(8802)
# connection to hostname on the port.
s.connect((host, port))
# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    #print ( "Number of joysticks: %i" %joystick_count)


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
            message +=":"+str(int(axis*100*2.556))
            #print ("warotsc z axis 0 : %f" %joystick.get_axis(i))
            #print (" ")


        buttons = joystick.get_numbuttons()
        #print ( "Number of buttons: %i "%buttons)

        message+=";button"
        for i in range(buttons):
            button = joystick.get_button(i)
            #print ( "Button %i" %i )
            #print (" value: %s " %button)
            message+=":"+str(i)+"="+str(button)
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        #print ( "Number of hats: %i" %hats)

        message+=";hets"
        for i in range(hats):
            hat = joystick.get_hat(i)
            #print (  "Hat %i " %i )
            #print (" value: %s " %str(hat))
            message+=":"+str(i)+"="+str(hat)

        message+=";END"
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.


    # Limit to 60 frames per second
    print (message)
    print ("wielkosc %i" %len(message))
    s.send (message)
    print(" odbieramy")
    tm = s.recv(256)
    print ("odebrano: ")
    print(tm)
    clock.tick(30)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()