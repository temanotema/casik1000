import sys
import pygame

# Создание главного меню
pygame.init()
# Инициализация  окна
WIN_WIDTH = 1280
WIN_HEIGHT = 720
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
black = (0, 0, 0)
white = (255, 255, 255)

# Инициализация текстов и счетов
GUI_font = pygame.font.SysFont(None, 32)
WIN_font = pygame.font.SysFont(None, 42)
INST_font = pygame.font.SysFont(None, 30)
TITLE_font = pygame.font.SysFont(None, 24)


# Трансформация картинок
def load_image(path, size):
    return pygame.transform.scale(pygame.image.load(path), size)

# Выгрузка фото
lemon = load_image('images/lemon.jpg', (200, 200))
apple = load_image('images/apple.jpg', (200, 200))
plum = load_image('images/plum.jpg', (200, 200))
cherry = load_image('images/cherry.jpg', (200, 200))


# Шрифт
def get_font(size):
    return pygame.font.Font("pics/font.ttf", size)

# Функция выхода
def quit():
    pygame.quit()
    sys.exit()


IMAGE_BLACKJACK = pygame.image.load("pics/blackjack.png")
IMAGE_BG = pygame.image.load("pics/Background.png")

# Управление функциями запуска окон
run = {}
MENU_MAIN = "main menu"
MENU_TWO = 'two menu'
GAME_BLACKJACK = "blackjack"
GAME_LUCKYSEVEN = "luckyseven"
