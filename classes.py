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
        self.button_text = font.render(button_text, True,color=(20,20,20))

