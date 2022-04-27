import sys
from casik.button import Button
from casik.pygame_base import *


PLAY_TEXT = get_font(100).render("Choose your game:", True, "#b68f40")
PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
PLAY_BACK = Button(image=None, pos=(640, 650),
                   text_input="BACK", font=get_font(75), base_color="Red", hovering_color="White")
BLACKJACK_BUTTON = Button(image=pygame.image.load('pics/blackjack.png'), pos=(320, 360),
                          text_input="Black Jack", font=get_font(55), base_color="Black", hovering_color="Green")
LUCKYSEVEN_BUTTON = Button(image=pygame.image.load("pics/slot.png"), pos=(960, 360),
                           text_input="Lucky Seven", font=get_font(55), base_color="Black", hovering_color="Green")


# Второе окно
def game_select():
    next_function = None
    while not next_function:
        win.blit(IMAGE_BG, (0, 0))
        win.blit(IMAGE_BLACKJACK, (170, 210))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        win.blit(PLAY_TEXT, PLAY_RECT)
        BLACKJACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        BLACKJACK_BUTTON.update(win)
        LUCKYSEVEN_BUTTON.changeColor(PLAY_MOUSE_POS)
        LUCKYSEVEN_BUTTON.update(win)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                next_function = quit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    next_function = main
                if BLACKJACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    next_function = run[GAME_BLACKJACK]
                if LUCKYSEVEN_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    next_function = run[GAME_LUCKYSEVEN]
        pygame.display.update()
    if next_function:
        next_function()


# Настройки
def options():
    next_function = None
    while not next_function:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        win.fill("white")

        OPTIONS_TEXT = get_font(45).render("Options.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        win.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 400),
                            text_input="Back", font=get_font(75), base_color="Black", hovering_color="Red")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                next_function = quit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    next_function = main
        pygame.display.update()

    if next_function:
        next_function()


MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
PLAY_BUTTON = Button(image=pygame.image.load("pics/play.png"), pos=(640, 250),
                     text_input="PLAY", font=get_font(75), base_color="#d4ebfc", hovering_color="Green")
OPTIONS_BUTTON = Button(image=pygame.image.load("pics/settings.png"), pos=(640, 400),
                        text_input="OPTIONS", font=get_font(75), base_color="#d4ebfc", hovering_color="Green", )
QUIT_BUTTON = Button(image=pygame.image.load("pics/quit.png"), pos=(640, 550),
                     text_input="QUIT", font=get_font(75), base_color="#d4ebfc", hovering_color="Red")


# Первое окно
def main():
    pygame.display.set_caption("CASINO")
    next_function = None
    while not next_function:
        win.blit(IMAGE_BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        win.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(win)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    next_function = game_select
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    next_function = options
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    next_function = quit

        pygame.display.update()
    if next_function:
        next_function()


run[MENU_MAIN] = main
run[MENU_TWO] = game_select

