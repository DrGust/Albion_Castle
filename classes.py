import random
import time
import pygame
from pygame import color


class Button:
    def __init__(self, x, y, width, height, name, onclick_function,button_text='Button'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.onclick_function = onclick_function
        font=pygame.font.Font(None,20)
        self.button_text = font.render(button_text, True,color=(20,20,20))
        self.buttonSurface = pygame.Surface((self.width,self.height))
        self.buttonRect = pygame.Rect(self.x,self.y,self.width,self.height)

    def draw_button(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.buttonRect.collidepoint(mouse_pos):
            bg_color = (230,230,250)
            border_color = (120,120,120)
        else:
            bg_color = (200,200,200)
            border_color = (120,120,120)

        pygame.draw.rect(screen,bg_color,self.buttonRect, border_radius=12)