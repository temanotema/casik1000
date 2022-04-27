from casik.pygame_base import *
from casik.button import Button
import random

# Данные карт
CARD_VALUES = [11,2,3,4,5,6,7,8,9,10,10,10,10]
CARD_NAMES = list(range(1,14))
CARD_SUITS = list(range(1,5))

# Размер карт
CARD_WIDTH = 150
CARD_HEIGHT = 250

card_img_dir = []
card_img = []

# Цвета
black = (0,0,0)
white = (255,255,255)


# Создание карт
class Card():
    def __init__(self,V,N,S,P):
        self.value = V      # Очко карты
        self.name = N       # Навание карты
        self.suit = S       # Обложкка карты
        self.image = P      # Рисунок карты


# Создание колоды
def initializeDeck():
    deck = []
    i = 0
    for j in range(len(CARD_VALUES)):
        for k in CARD_SUITS:
            deck.append(Card(CARD_VALUES[j], CARD_NAMES[j], k, card_img[i]))
            i += 1

    return deck


# Поиск карты
def card_index(V,S):
    if S == 'S':
        T = 1
    elif S == 'C':
        T = 2
    elif S == 'D':
        T = 3
    elif S == 'H':
        T = 4
    else:
        print("Error with T in card_index()")

    return (V-1)*4 + (T-1)


# Отображение карт на экране
def display_card():
    # Показать каждую карту
    if (len( player_hand) != 0):
        for i in range(len( player_hand)):
            win.blit( player_hand[i].image, (card_x_pos[i],card_y_pos[i]))

    if(reveal or spectate):
        # Лицевой стороной у оппонента
        if (len( AI_hand) != 0):
            for i in range(len( AI_hand)):
                win.blit( AI_hand[i].image, (AI_card_x_pos[i],AI_card_y_pos[i]))
    else:
        # Обратной стороной у оппонента
        if (len( hidden_hand) != 0):
            for i in range(len( hidden_hand)):
                win.blit( hidden_hand[i].image, (hidden_card_x_pos[i],hidden_card_y_pos[i]))

    pygame.display.update()


# Случайный выбор карты
def get_random_card():
    global full_deck
    r = random.randint(0,len(full_deck)-1)

    return full_deck.pop(r)


# Положить карту игроку
def player_draw_cards():
    global card_x_pos
    global card_y_pos

    # Добавить карту игроку
    player_hand.append(get_random_card())

    # Добавить новую позицию карте
    if (len(card_x_pos) == 0):
        card_x_pos.append(DEFAULT_X)
    else:
        card_x_pos.append(card_x_pos[-1] + DEFAULT_OFFSET)

    card_y_pos.append(DEFAULT_Y)


# Добавить карту оппоненту
def AI_draw_card():
    global AI_card_x_pos
    global AI_card_y_pos
    global hidden_card_x_pos
    global hidden_card_y_pos

    # Если значениу у оппа меньше 18 берет карту
    if get_card_value(AI_hand) < 18:
        AI_hand.append(get_random_card())
        hidden_hand.append(bg_card)

        # Добавить карту оппоненту, если ничего нет
        if (len(AI_card_x_pos) == 0):
            AI_card_x_pos.append(DEFAULT_X)
            hidden_card_x_pos.append(DEFAULT_X)
        else:
            # Добавить карту к предыдущей
            AI_card_x_pos.append(AI_card_x_pos[-1] + DEFAULT_OFFSET)
            hidden_card_x_pos.append(hidden_card_x_pos[-1] + DEFAULT_OFFSET)

        # Все карты значение Y
        AI_card_y_pos.append(AI_DEFAULT_Y)
        hidden_card_y_pos.append(AI_DEFAULT_Y)

        # Оппонент взял карту?
        return True
    else:
        return False


# Текущий счет игроков
def get_card_value(hand):
    # Если рука пустая вернуть ноль
    if len(hand) == 0:
        return 0
    else:
        Aces = []
        sum = 0

        # Пройти всю руку
        for i in hand:
            # Сколько тузов в руке
            if i.name == 1:
                Aces.append(i)

            # Суммирование очков
            sum += i.value

        # Уменьшение очков за туз
        if sum > 21 and (len(Aces) != 0):
            sum -= 10
        return sum


# Отображение текстов
def draw_texts():
    # Отображение меню текста
    ai_hand_text = GUI_font.render("ОППОНЕНТ:",True,white)
    player_hand_text = GUI_font.render("ВЫ:",True,white)
    hand_value_text = GUI_font.render('СУММА: '+ str(get_card_value(player_hand)),True,white)
    winner_text = WIN_font.render(win_str[win_int],True,white)

    win.blit(winner_text, (WIN_WIDTH//2-win_x[win_int], WIN_HEIGHT//2-win_y[win_int]))
    win.blit(hand_value_text, (175,WIN_HEIGHT-CARD_HEIGHT-60))
    win.blit(ai_hand_text, (15,15))
    win.blit(player_hand_text, (15,WIN_HEIGHT-CARD_HEIGHT-60))

    # Отображение инструкции
    r_text = INST_font.render('Нажмите [R] чтобы перезагрузить', True, white)
    space_text = INST_font.render('Нажмите [SPACE] чтобы взять', True, white)
    enter_text = INST_font.render('Нажмите [ENTER] чтобы пасануть', True, white)
    spec_text = INST_font.render('Нажмите [TAB] чтобы видеть очки', True, white)

    win.blit(r_text, (WIN_WIDTH//2+211,WIN_HEIGHT//2 - 330))
    win.blit(space_text, (WIN_WIDTH//2+211,WIN_HEIGHT//2 - 300))
    win.blit(enter_text, (WIN_WIDTH//2+211,WIN_HEIGHT//2 - 270))
    win.blit(spec_text, (WIN_WIDTH//2+211,WIN_HEIGHT//2 - 240))

    # Отображение счета оппанента если читы
    if spectate:
        AI_value_text = GUI_font.render('СУММА: '+ str(get_card_value(AI_hand)),True,white)
        win.blit(AI_value_text, (175,15))


# Загрузка фотографий карт
for i in CARD_NAMES:
    for j in CARD_SUITS:
        card_img_dir.append("images/" + str(i) + "-" + str(j) + ".png")

for i in card_img_dir:
    card_img.append(pygame.transform.scale(pygame.image.load(i), (CARD_WIDTH, CARD_HEIGHT)))

bg_card = Card(0,0,0,pygame.transform.scale(pygame.image.load("images/blue_back.png"), (CARD_WIDTH, CARD_HEIGHT)))

DEFAULT_X = 30
DEFAULT_Y = WIN_HEIGHT-CARD_HEIGHT-30
AI_DEFAULT_Y = 45
DEFAULT_OFFSET = 30

win_int = 0
win_str = ['', 'ВЫ ВЫИГРАЛИ', 'ОППОНЕНТ ВЫИГРАЛ', 'ПЕРЕБОР — ОППОНЕНТ ВЫИГРАЛ', 'ВЫ ВЫИГРАЛИ — ПЕРЕБОР', 'НИЧЬЯ', 'НЕТ ПОБЕДИТЕЛЯ']
win_x = [0, 100, 65, 180, 180, 40, 100]
win_y = [0, 30, 30, 30, 30, 30, 30]

original_deck = initializeDeck()
BG = pygame.image.load("pics/Background.png")

# Инициализация колод
player_hand = []
card_x_pos = []
card_y_pos = []

AI_hand = []
AI_card_x_pos = []
AI_card_y_pos = []

hidden_hand = []
hidden_card_x_pos = []
hidden_card_y_pos = []

# Булевые значекния для гуи
main_loop = 0
reveal = False
session = True
spectate = False
full_deck = []


# Рестарт окна
def reset_game():
    player_hand.clear()
    card_x_pos.clear()
    card_y_pos.clear()

    AI_hand.clear()
    AI_card_x_pos.clear()
    AI_card_y_pos.clear()

    hidden_hand.clear()
    hidden_card_x_pos.clear()
    hidden_card_y_pos.clear()

    global main_loop, reveal, session, spectate, orignal_deck, full_deck, win_int
    main_loop = 0
    reveal = False
    session = True
    spectate = False
    win_int = 0

    # Создание колоды, чтобы сохранить исходную копию
    full_deck = list(original_deck)


#Игра
def main():
    pygame.display.set_caption("BlackJack")

    global main_loop, session, spectate, win_int, reveal
    reset_game()
    next_function = None
    while not next_function:
        win.blit(IMAGE_BG, (0, 0))
        pygame.time.delay(100)
        SEVEN_MOUSE_POS = pygame.mouse.get_pos()

        SEVEN_BACK = Button(image=None, pos=(1100, 650),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")

        SEVEN_BACK.changeColor(SEVEN_MOUSE_POS)
        SEVEN_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                next_function = quit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SEVEN_BACK.checkForInput(SEVEN_MOUSE_POS):
                    next_function = run[MENU_TWO]
        draw_texts()
        pygame.display.update()

        # Антиспам кнопок
        if main_loop > 0:
            main_loop += 1
        if main_loop > 5:
            main_loop = 0

        # Получение нажатых клавиш
        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            reset_game()

        # Игрок взял или получил другую карту
        if keys[pygame.K_SPACE] and main_loop == 0 and session:
            player_draw_cards()
            main_loop = 1

            AI_draw_card()

            print("ОППОНЕНТ: ", end='')
            print(get_card_value(AI_hand))

            # Все возможные результаты
            if get_card_value(AI_hand) > 21 and get_card_value(player_hand) > 21:
                session = False
                print("НЕТ ПОБЕДИТЕЛЯ")
                win_int = 6
                reveal = True
            elif get_card_value(AI_hand) > 21:
                session = False
                print("ПЕРЕБОР, ВЫ ВЫИГРАЛИ!")
                win_int = 4
                reveal = True
            elif get_card_value(player_hand) > 21:
                print('ПЕРЕБОР, ОППОНЕНТ ВЫИГРАЛ!')
                win_int = 3
                session = False
                reveal = True
            elif get_card_value(AI_hand) == 21 and get_card_value(player_hand) == 21:
                print('НИЧЬЯ')
                win_int = 5
                session = False
                reveal = True
            elif get_card_value(AI_hand) == 21 and get_card_value(player_hand) != 21:
                print('ОППОНЕНТ ВЫИГРАЛ!')
                win_int = 2
                session = False
                reveal = True
            elif get_card_value(AI_hand) != 21 and get_card_value(player_hand) == 21:
                print('ВЫ ВЫИГРАЛИ!')
                win_int = 1
                session = False
                reveal = True

        # Игрок пасует
        if (keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]) and main_loop == 0 and session:
            main_loop = 1

            AI_hit = AI_draw_card()

            print("ОППОНЕНТ: ", end='')
            print(get_card_value(AI_hand))

            # Все возможные результаты
            if (AI_hit == False):
                if get_card_value(AI_hand) > get_card_value(player_hand):
                    session = False
                    print("ОППОНЕНТ ВЫИГРАЛ")
                    win_int = 2
                    reveal = True
                elif get_card_value(AI_hand) < get_card_value(player_hand):
                    session = False
                    print("ВЫ ВЫИГРАЛИ")
                    win_int = 1
                    reveal = True
                else:
                    session = False
                    print("TIED")
                    win_int = 5
                    reveal = True
            else:
                if get_card_value(AI_hand) > 21 and get_card_value(player_hand) > 21:
                    session = False
                    print("НЕТ ПОБЕДИТЕЛЯ")
                    win_int = 6
                    reveal = True
                elif get_card_value(AI_hand) > 21:
                    session = False
                    print("ПЕРЕБОР, ВЫ ВЫИГРАЛИ")
                    win_int = 4
                    reveal = True
                elif get_card_value(AI_hand) == 21 and get_card_value(player_hand) == 21:
                    print('НИЧЬЯ')
                    win_int = 5
                    session = False
                    reveal = True
                elif get_card_value(AI_hand) == 21 and get_card_value(player_hand) != 21:
                    print('ОППОНЕНТ ВЫИГРАЛ!')
                    win_int = 2
                    session = False
                    reveal = True
                elif get_card_value(AI_hand) != 21 and get_card_value(player_hand) == 21:
                    print('ВЫ ВЫИГРАЛИ!')
                    win_int = 1
                    session = False
                    reveal = True

        # Режим наблюдателя
        if keys[pygame.K_TAB] and main_loop == 0:
            if spectate == False:
                spectate = True
            else:
                spectate = False

            main_loop = 1

        display_card()
    if next_function:
        next_function()


run[GAME_BLACKJACK] = main

