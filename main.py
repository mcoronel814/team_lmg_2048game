import pygame
import random
import time
import numpy as np

BG_COLORS = {
        0: (255, 255, 255),
        2: (192, 46, 29),
        4: (217, 78, 31),
        8: (241, 108, 32),
        16: (239, 139, 44),
        32: (236, 170, 56),
        64: (235, 200, 68),
        128: (164, 187, 108),
        256: (92, 167, 147),
        512: (19, 149, 186),
        1024: (17, 120, 153),
        2048: (15, 91, 120),
        "white": (255, 255, 255)
    }
BLUE = {
        0: (220, 236, 201),
        2: (179, 221, 204),
        4: (138, 205, 206),
        8: (98, 190, 210),
        16: (70, 170, 206),
        32: (61, 145, 190),
        64: (53, 119, 174),
        128: (45, 94, 158),
        256: (36, 68, 142),
        512: (28, 43, 127),
        1024: (22, 32, 101),
        2048: (17, 23, 75),
        "black": (0, 0, 0)

    }

ORANGE = {
        0: (255, 255, 255),
        2: (253, 232, 110),
        4: (249, 208, 99),
        8: (245, 184, 87),
        16: (240, 160, 75),
        32: (235, 138, 64),
        64: (231, 114, 53),
        128: (227, 91, 44),
        256: (199, 78, 41),
        512: (157, 68, 41),
        1024: (117, 60, 44),
        2048: (76, 52, 48),
        "black": (62, 75, 75)

    }

PINK = {
        0: (214, 214, 214),
        2: (243, 172, 162),
        4: (238, 139, 151),
        8: (233, 106, 141),
        16: (219, 80, 135),
        32: (184, 66, 140),
        64: (151, 52, 144),
        128: (116, 39, 150),
        256: (94, 31, 136),
        512: (77, 26, 112),
        1024: (61, 20, 89),
        2048: (45, 15, 65),
        "black": (62, 75, 75)

    }



class game_2048:
    def __init__(self):
        self.board_length = 4
        self.cell_size = 100
        self.gap = 6
        self.window_bg_color = (187, 173, 160)
        self.block_size = self.cell_size + self.gap * 2

        self.window_width = self.block_size * 6
        self.window_height = self.block_size * 4
        self.window_bg_img = pygame.image.load('2048_title_hotpink.png')

        pygame.init()

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.myFont = pygame.font.SysFont("Book Script", 30)
        pygame.display.set_caption('2048 - Brought to you by LMG')
        self.start_time = 0
        self.score = 0

        # start the board with zeros and random number
        self.board_status = np.zeros((self.board_length, self.board_length))
        self.add_new_number()
        #self.pink_back = pygame.image.load("new_left.png").convert_alpha()

    def intro(self):
        background_colour = PINK[16]
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        screen.fill(background_colour)
        pygame.display.flip()

        X = self.window_width
        Y = self.window_height
        screen = pygame.display.set_mode((X, Y))
        INTRO_TICK = 0.25

        image1 = pygame.image.load("LMG_Logo_57.png")
        image1 = pygame.transform.scale(image1, (X, Y))
        screen.blit(image1, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(INTRO_TICK)

        image2 = pygame.image.load("LMG_Logo_58.png")
        image2 = pygame.transform.scale(image2, (X, Y))
        screen.blit(image2, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(INTRO_TICK)

        image3 = pygame.image.load("LMG_Logo_59.png")
        image3 = pygame.transform.scale(image3, (X, Y))
        screen.blit(image3, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(INTRO_TICK)

        image4 = pygame.image.load("LMG_Logo_60.png")
        image4 = pygame.transform.scale(image4, (X, Y))
        screen.blit(image4, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(0.01)

        text_intro = self.myFont.render('2048 - brought to you by LMG', True, 'Black', BG_COLORS[0])
        textRect = text_intro.get_rect()
        textRect.center = (X // 1.30, Y // 1.02)
        screen.blit(text_intro, textRect)
        pygame.display.flip()
        time.sleep(1)

    def draw_button(self, screen_var, button_color, x_button, y_button, draw_width, draw_height, text_var,
                    text_color_var):
        smallfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = smallfont.render(text_var, True, text_color_var)
        pygame.draw.rect(screen_var, button_color, [x_button, y_button, draw_width, draw_height])
        screen_var.blit(text, (x_button + 50, y_button))
        # pygame.display.update()

    def main_menu(self):
        background_colour = PINK[16]
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        screen.fill(background_colour)
        pygame.display.flip()

        X = self.window_width
        Y = self.window_height
        X_COORD = X / 2
        Y_COORD = Y / 2
        BUTTON_HEIGHT = 40
        BUTTON_WIDTH = 250
        BUTTON_GAP = BUTTON_HEIGHT * 1.15
        DROPDOWN_WIDTH = 50
        #DROPDOWN_LEFT_PADDING =
        screen = pygame.display.set_mode((X, Y))

        text_color = (PINK[0])
        button_bg_color = (PINK[64])
        hover_color = (PINK[32])

        # smallfont = pygame.font.SysFont('Comic Sans MS', 30)
        # text = smallfont.render('New Game', True, text_color)

        while True:


            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if X_COORD <= mouse[0] <= X_COORD + BUTTON_WIDTH and Y_COORD <= mouse[1] <= Y_COORD + BUTTON_HEIGHT:
                        game = game_2048()
                        game.play()

 #               if ev.type == pygame.MOUSEBUTTONDOWN:
                    elif X_COORD <= mouse[0] <= X_COORD + BUTTON_WIDTH and Y_COORD <= mouse[1] <= Y_COORD + BUTTON_HEIGHT:
                        game = game_2048()
                        game.play()
                #Add "If" : mouse is over button2 when clicked, then display themes
#####==================
                    elif X_COORD <= mouse[0] <= X_COORD + BUTTON_WIDTH and (Y_COORD + BUTTON_GAP) <= mouse[1] <= (Y_COORD + BUTTON_HEIGHT + BUTTON_GAP):
                        self.window.fill("yellow")
                        theme_message = self.myFont.render("Select a theme:", False, "brown")
                        self.draw_button(screen, button_bg_color, X_COORD, Y_COORD, BUTTON_WIDTH,
                                         BUTTON_HEIGHT, "Theme 1", text_color)
                        self.draw_button(screen, button_bg_color, X_COORD, Y_COORD + BUTTON_GAP, BUTTON_WIDTH,
                                         BUTTON_HEIGHT, "Theme 2", text_color)
                        self.draw_button(screen, button_bg_color, X_COORD, Y_COORD + BUTTON_GAP*2, BUTTON_WIDTH,
                                         BUTTON_HEIGHT, "Theme 3", text_color)
                        self.window.blit(theme_message, (250, 100))
                        pygame.display.flip()
                        mouse = pygame.mouse.get_pos()
                        pygame.display.update()
                        pygame.display.flip()
                        #time.sleep(4)

                    time.sleep(4)

#####==================
            screen.fill((228, 203, 194))
            self.window.blit(self.window_bg_img, self.window_bg_img.get_rect())
            mouse = pygame.mouse.get_pos()

            if X_COORD <= mouse[0] <= X_COORD + BUTTON_WIDTH and Y_COORD <= mouse[1] <= Y_COORD + BUTTON_HEIGHT:
                self.draw_button(screen, hover_color, X_COORD, Y_COORD, BUTTON_WIDTH, BUTTON_HEIGHT, "New Game",
                                 text_color)
                self.draw_button(screen, button_bg_color, X_COORD, Y_COORD + BUTTON_GAP, BUTTON_WIDTH,
                                 BUTTON_HEIGHT, "Change Theme", text_color)
                pygame.display.update()
            elif X_COORD <= mouse[0] <= X_COORD + BUTTON_WIDTH and (Y_COORD + BUTTON_GAP) <= mouse[1] <= (
                    Y_COORD + BUTTON_HEIGHT + BUTTON_GAP):
                self.draw_button(screen, hover_color, X_COORD, Y_COORD + BUTTON_GAP, BUTTON_WIDTH, BUTTON_HEIGHT,
                                 "Change Theme", text_color)
                self.draw_button(screen, button_bg_color, X_COORD, Y_COORD, BUTTON_WIDTH, BUTTON_HEIGHT, "New Game",
                                 text_color)
                pygame.display.update()
            else:
                self.draw_button(screen, button_bg_color, X_COORD, Y_COORD, BUTTON_WIDTH, BUTTON_HEIGHT, "New Game",
                                 text_color)
                self.draw_button(screen, button_bg_color, X_COORD, Y_COORD + BUTTON_GAP, BUTTON_WIDTH,
                                 BUTTON_HEIGHT, "Change Theme", text_color)
                pygame.display.update()

    def add_new_number(self):
        empty_space = zip(*np.where(self.board_status == 0))
        empty_space = list(empty_space)

        for position in random.sample(empty_space, k=1):
            self.board_status[position] = 2


    def glow(self,image):
        transform_image= pygame.transform.scale(pygame.image.load(image), (300, 300))
        return transform_image

    def draw_board(self):
        self.pink = self.glow("glow-pink-3.png")
        self.start_time = 7
        self.window.fill(self.window_bg_color)
        pink_back = pygame.image.load("pink_back.png")
        image_end = pygame.transform.scale(pink_back, (self.window_width, self.window_height))
        self.window.blit(image_end, (0, 0))
        if self.game_over():
            image_end = pygame.image.load("end_screen.png")
            ending_message = pygame.image.load("game_over_im.png")
            game_over_end = pygame.transform.scale(ending_message, (325, 175))
            image_end = pygame.transform.scale(image_end, (self.window_width, self.window_height))

            space_press = pygame.image.load("space.press.png").convert_alpha()
            space_pressed = pygame.transform.scale(space_press, (400, 120))
            space_rect = space_pressed.get_rect(bottomright=(540, 420))

            self.window.blit(image_end, (0, 0))
            self.window.blit(game_over_end, (170, 90))
            self.window.blit(space_pressed, space_rect)
            pygame.display.update()
        else:
            up_button = pygame.image.load("new_up.png").convert_alpha()
            up_arrow = pygame.transform.scale(up_button, (50, 50))
            up_rect = up_arrow.get_rect(bottomright=(575, 385))

            down_button = pygame.image.load("new_down.png").convert_alpha()
            down_arrow = pygame.transform.scale(down_button, (50, 50))
            down_rect = down_arrow.get_rect(bottomright=(575, 440))

            right_button = pygame.image.load("new_right.png").convert_alpha()
            right_arrow = pygame.transform.scale(right_button, (50, 50))
            right_rect = right_arrow.get_rect(bottomright=(630, 440))

            left_button = pygame.image.load("new_left.png").convert_alpha()
            left_arrow = pygame.transform.scale(left_button, (50, 50))
            left_rect = left_arrow.get_rect(bottomright=(520, 440))

            menu_img = pygame.image.load("MENU.png").convert_alpha()
            menu_size = pygame.transform.scale(menu_img, (45, 20))
            menu_rect = menu_size.get_rect(bottomright=(650, 255))

            pause_img = pygame.image.load("PAUSE.png").convert_alpha()
            pause_size = pygame.transform.scale(pause_img, (45, 20))
            pause_rect = pause_size.get_rect(bottomright=(650, 280))

            theme_img = pygame.image.load("THEME.png").convert_alpha()
            theme_size = pygame.transform.scale(theme_img, (45, 20))
            theme_rect = theme_size.get_rect(bottomright=(650, 307))

            scores_img = pygame.image.load("SCORES.png").convert_alpha()
            scores_size = pygame.transform.scale(scores_img, (45, 20))
            scores_rect = scores_size.get_rect(bottomright=(650, 333))

            quit_img = pygame.image.load("QUIT.png").convert_alpha()
            quit_size = pygame.transform.scale(quit_img, (45, 20))
            quit_rect = quit_size.get_rect(bottomright=(650, 360))

            current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
            time_surf = self.myFont.render(f'Time Played: {current_time}', False, (255, 255, 255))
            time_rect = time_surf.get_rect(center=(550, 200))

            score_surf = self.myFont.render(f'Score: {self.score}', False, (255, 255, 255))
            score_rect = score_surf.get_rect(center=(600, 150))

            self.window.blit(up_arrow, up_rect)
            self.window.blit(down_arrow, down_rect)
            self.window.blit(right_arrow, right_rect)
            self.window.blit(left_arrow, left_rect)

            pygame.draw.rect(self.window, "pink", time_rect)
            self.window.blit(time_surf, time_rect)
            pygame.draw.rect(self.window, "pink", score_rect)
            self.window.blit(score_surf, score_rect)

            self.window.blit(menu_size, menu_rect)
            self.window.blit(pause_size, pause_rect)
            self.window.blit(theme_size, theme_rect)
            self.window.blit(quit_size, quit_rect)
            self.window.blit(scores_size, scores_rect)

            for r in range(self.board_length):
                rect_y = self.block_size * r + self.gap
                for c in range(self.board_length):
                    rect_x = self.block_size * c + self.gap
                    cell_value = int(self.board_status[r][c])

                    pygame.draw.rect(
                        self.window,
                        PINK[cell_value],
                        pygame.Rect(rect_x, rect_y, self.cell_size, self.cell_size)
                    )

                    if cell_value > 8:
                        self.window.blit(self.pink, (rect_x-100, rect_y-80))



                    if cell_value != 0:
                        text_surface = self.myFont.render(f"{cell_value}", True, PINK["black"])
                        text_rect = text_surface.get_rect(
                            center=(rect_x + self.block_size / 2, rect_y + self.block_size / 2))
                        self.window.blit(text_surface, text_rect)

    def merge_numbers_test(self, data):
        result = [0]
        data = [x for x in data if x != 0]
        for element in data:
            if element == result[len(result) - 1]:
                result[len(result) - 1] *= 2
                result.append(0)
            else:
                result.append(element)
        result = [x for x in result if x != 0]
        return result

    def merge_numbers(self, data):
        result = [0]
        data = [x for x in data if x != 0]
        for element in data:
            if element == result[len(result) - 1]:
                result[len(result) - 1] *= 2
                self.score += int(result[len(result) - 1])
                result.append(0)
            else:
                result.append(element)
        result = [x for x in result if x != 0]
        return result

    def movement_test(self, direction):
        for index in range(self.board_length):

            if direction in "UD":
                data = self.board_status[:, index]
            else:
                data = self.board_status[index, :]

            flip = False
            if direction in "RD":
                flip = True
                data = data[::-1]

            data = self.merge_numbers_test(data)
            data = data + (self.board_length - len(data)) * [0]

            if flip:
                data = data[::-1]

            if direction in "UD":
                self.board_status[:, index] = data
            else:
                self.board_status[index, :] = data

    def movement(self, direction):
        for index in range(self.board_length):

            if direction in "UD":
                data = self.board_status[:, index]
            else:
                data = self.board_status[index, :]

            flip = False
            if direction in "RD":
                flip = True
                data = data[::-1]

            data = self.merge_numbers(data)
            data = data + (self.board_length - len(data)) * [0]

            if flip:
                data = data[::-1]

            if direction in "UD":
                self.board_status[:, index] = data
            else:
                self.board_status[index, :] = data

    def game_over(self):
        board_status_backup = self.board_status.copy()
        for direction in "UDLR":
            self.movement_test(direction)

            if not (self.board_status == board_status_backup).all():
                self.board_status = board_status_backup
                return False
        return True

    def play(self):
        running = True
        while running:
            self.draw_board()
            pygame.display.update()

            for event in pygame.event.get():
                old_board_status = self.board_status.copy()

                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement("U")
                    elif event.key == pygame.K_DOWN:
                        self.movement("D")
                    elif event.key == pygame.K_LEFT:
                        self.movement("L")
                    elif event.key == pygame.K_RIGHT:
                        self.movement("R")
                    elif event.key == pygame.K_ESCAPE:
                        running = False

                    if not (self.board_status == old_board_status).all():
                        self.add_new_number()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    up_button = pygame.image.load("new_up.png").convert_alpha()
                    up_arrow = pygame.transform.scale(up_button, (50, 50))
                    up_rect = up_arrow.get_rect(bottomright=(575, 385))

                    down_button = pygame.image.load("new_down.png").convert_alpha()
                    down_arrow = pygame.transform.scale(down_button, (50, 50))
                    down_rect = down_arrow.get_rect(bottomright=(575, 440))

                    right_button = pygame.image.load("new_right.png").convert_alpha()
                    right_arrow = pygame.transform.scale(right_button, (50, 50))
                    right_rect = right_arrow.get_rect(bottomright=(630, 440))

                    left_button = pygame.image.load("new_left.png").convert_alpha()
                    left_arrow = pygame.transform.scale(left_button, (50, 50))
                    left_rect = left_arrow.get_rect(bottomright=(520, 440))

                    menu_img = pygame.image.load("MENU.png").convert_alpha()
                    menu_size = pygame.transform.scale(menu_img, (45, 20))
                    menu_rect = menu_size.get_rect(bottomright=(650, 255))

                    pause_img = pygame.image.load("PAUSE.png").convert_alpha()
                    pause_size = pygame.transform.scale(pause_img, (45, 20))
                    pause_rect = pause_size.get_rect(bottomright=(650, 280))

                    theme_img = pygame.image.load("THEME.png").convert_alpha()
                    theme_size = pygame.transform.scale(theme_img, (45, 20))
                    theme_rect = theme_size.get_rect(bottomright=(650, 307))

                    scores_img = pygame.image.load("SCORES.png").convert_alpha()
                    scores_size = pygame.transform.scale(scores_img, (45, 20))
                    scores_rect = scores_size.get_rect(bottomright=(650, 333))

                    quit_img = pygame.image.load("QUIT.png").convert_alpha()
                    quit_size = pygame.transform.scale(quit_img, (45, 20))
                    quit_rect = quit_size.get_rect(bottomright=(650, 360))

                    if up_rect.collidepoint(event.pos):
                        self.movement("U")
                    if down_rect.collidepoint(event.pos):
                        self.movement("D")
                    if right_rect.collidepoint(event.pos):
                        self.movement("R")
                    if left_rect.collidepoint(event.pos):
                        self.movement("L")

                    if not (self.board_status == old_board_status).all():
                        self.add_new_number()


if __name__ == "__main__":
    game = game_2048()
    game.intro()
    game.main_menu()
    game.play()
