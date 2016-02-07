# -*- coding: cp1252 -*-
#/usr/bin/env python
#Simon H. Larsen
#Buttons
#Project startet: d. 26. august 2012
import pygame
from pygame.locals import *
import func
import time
pygame.init()
class Button:
    
    # tworzy przycisk  i go rysuje 
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface
    
    # wypisuje tkest na przycisku 
    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length//len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface
    
    # rysowanie przycisku
    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface
    
    # czy przycisk jest wcisniety 
    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print "Some button was pressed!"
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

class dialog_box:

    def __init__(self):
        print " tworze obietk"
    def __enter__(self):
        print "kasuje obiekt"
    def draw_box (self,wher,color,color_txt,text,screen):
        self.rect = pygame.draw.rect(screen,color, wher)
        func.print_value(screen,text,"Arial",wher[3] -(wher[3]/6),color_txt,wher[0],wher[1])
    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print "wpisz hosta!"

                        return True
                    else: return False
                else: return False
            else: return False
        else: return False