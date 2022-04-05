import pygame, sys
from button import Button
from enum import Enum, IntEnum
import random
from pics import *

pygame.init()

WIN_WIDTH = 1280
WIN_HEIGHT = 720
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("LuckySeven")

main_loop = 0
run_game = True

BG = pygame.image.load("pics/Background.png")
black = (0, 0, 0)
white = (255, 255, 255)
INST_font = pygame.font.SysFont(None, 30)


def get_font(size):
    return pygame.font.Font("pics/font.ttf", size)


def draw_texts():
    space_text = INST_font.render('Нажмите [SPACE] чтобы прокрутить слот', True, white)
    combo1_text = INST_font.render('Комбинация 1: 7 | 7 | 7 ', True, white)
    combo2_text = INST_font.render('Комбинация 2: bell | bell | bell', True, white)
    combo3_text = INST_font.render('Комбинация 3: bar | bar | bar', True, white)
    combo4_text = INST_font.render('Комбинация 4: cherry | cherry | cherry', True, white)

    win.blit(combo1_text, (WIN_WIDTH // 2 + 211, WIN_HEIGHT // 2 - 330))
    win.blit(combo2_text, (WIN_WIDTH // 2 + 211, WIN_HEIGHT // 2 - 300))
    win.blit(combo3_text, (WIN_WIDTH // 2 + 211, WIN_HEIGHT // 2 - 270))
    win.blit(combo4_text, (WIN_WIDTH // 2 + 211, WIN_HEIGHT // 2 - 240))
    win.blit(space_text, (WIN_WIDTH // 2 + 211, WIN_HEIGHT // 2 - 210))



while run_game:
    win.blit(BG, (0, 0))
    pygame.time.delay(100)

    win.blit(BG, (0, 0))
    SEVEN_MOUSE_POS = pygame.mouse.get_pos()

    SEVEN_BACK = Button(image=None, pos=(1100, 650),
                        text_input="BACK", font=get_font(75), base_color="Red", hovering_color="White")

    SEVEN_BACK.changeColor(SEVEN_MOUSE_POS)
    SEVEN_BACK.update(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if SEVEN_BACK.checkForInput(SEVEN_MOUSE_POS):
                import main

    draw_texts()

    pygame.display.update()

pygame.quit()