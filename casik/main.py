import pygame, sys
from button import Button
import blackjack
import luckyseven


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("CASINO")
BLACKJACK = pygame.image.load("pics/blackjack.png")
BG = pygame.image.load("pics/Background.png")


def load_image(path, size):
    return pygame.transform.scale(pygame.image.load(path), size)


def get_font(size):
    return pygame.font.Font("pics/font.ttf", size)


PLAY_TEXT = get_font(100).render("Choose your game:", True, "#b68f40")

PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
PLAY_BACK = Button(image=None, pos=(640, 650),
                   text_input="BACK", font=get_font(75), base_color="Red", hovering_color="White")

BLACKJACK_BUTTON = Button(image=pygame.image.load('pics/blackjack.png'), pos=(320, 360),
                    text_input="Black Jack", font=get_font(55), base_color="Black", hovering_color="Green")

LUCKYSEVEN_BUTTON = Button(image=pygame.image.load("pics/slot.png"), pos=(960, 360),
                    text_input="Lucky Seven", font=get_font(55), base_color="Black", hovering_color="Green")
def play():
    next_function = None
    while not next_function:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(BLACKJACK, (170, 210))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        BLACKJACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        BLACKJACK_BUTTON.update(SCREEN)
        LUCKYSEVEN_BUTTON.changeColor(PLAY_MOUSE_POS)
        LUCKYSEVEN_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    next_function = main_menu
                if BLACKJACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    next_function = blackjack.main
                if LUCKYSEVEN_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    next_function = luckyseven.main
        pygame.display.update()
    if next_function:
        next_function()


def options():
    next_function = None
    while not next_function:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Options.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 400),
                            text_input="Back", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    next_function = main_menu
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


def main_menu():
    next_function = None
    while not next_function:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    next_function = play
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    next_function = options
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
    if next_function:
        next_function()

pygame.display.update()
main_menu()
