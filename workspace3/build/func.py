import pygame
import time
def print_value (screen, text, _font, font_size, color, _x, _y):
    my_font_value = pygame.font.SysFont(_font, font_size)
    screen.blit( my_font_value.render(text,1,color)     ,( _x, _y))
    
def joy_AND_connection( threadName, delay):
    count =0
    while count <30:
        time.sleep(delay)
        count += 1
        print "%s: %s"%( threadName, time.ctime(time.time()))
        