from casik.button import Button
from casik.pygame_base import *


SEVEN_BACK = Button(image=None, pos=(1100, 650),
                    text_input="BACK", font=get_font(75), base_color="Red", hovering_color="White")
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


def main():
    pygame.display.set_caption("LuckySeven")
    next_function = None

    while not next_function:
        win.blit(IMAGE_BG, (0, 0))
        SEVEN_MOUSE_POS = pygame.mouse.get_pos()
        SEVEN_BACK.changeColor(SEVEN_MOUSE_POS)
        SEVEN_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                next_function = quit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SEVEN_BACK.checkForInput(SEVEN_MOUSE_POS):
                    next_function = run[MENU_MAIN]
        draw_texts()
        pygame.display.update()
    if next_function:
        next_function()


run[GAME_LUCKYSEVEN] = main

if __name__ == "__main__":
    main()
