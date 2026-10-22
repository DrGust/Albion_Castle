import pygame
import random
import classes
import time

main_menu_check = False
game_has_started = False
break_menu_check = False

pygame.init()
screen = pygame.display.set_mode((1920, 1080))

game_start_button = classes.Button(x=960, y=400, width=200, height=100, name="start", button_text="Start", onclick_function= 'game_start')

def main_menu():
    global main_menu_check
    main_menu_check = True

def game_start():
    global game_has_started
    game_has_started = True