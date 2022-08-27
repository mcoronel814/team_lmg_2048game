import pygame
import random
import time
import numpy as np

BG_COLORS = {
    0: (255, 255, 255),
    2: (255, 215, 157),
    4: (217, 2, 238),
    8: (241, 98, 255),
    16: (50, 13, 62),
    32: (255, 223, 177),
    64: (232, 13, 253),
    128: (246, 149, 255),
    256: (101, 26, 125),
    512: (255, 229, 193),
    1024: (228, 2, 249),
    2048: (248, 175, 255)
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

        pygame.init()

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.myFont = pygame.font.SysFont("Book Script", 30)
        pygame.display.set_caption('2048 - Brought to you by LMG')
        self.start_time = 0
        self.score = 0

        # start the board with zeros and random number
        self.board_status = np.zeros((self.board_length, self.board_length))
        self.add_new_number()

        self.pink_back = pygame.image.load("new_left.png").convert_alpha()

    def intro(self):
        background_colour = BG_COLORS[16]
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        screen.fill(background_colour)
        pygame.display.flip()

        X = self.window_width
        Y = self.window_height
        screen = pygame.display.set_mode((X, Y))

        image1 = pygame.image.load("LMG_Logo_57.png")
        image1 = pygame.transform.scale(image1, (X, Y))
        screen.blit(image1, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(1)

        image2 = pygame.image.load("LMG_Logo_58.png")
        image2 = pygame.transform.scale(image2, (X, Y))
        screen.blit(image2, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(1)

        image3 = pygame.image.load("LMG_Logo_59.png")
        image3 = pygame.transform.scale(image3, (X, Y))
        screen.blit(image3, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(1)

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
        time.sleep(3)

    def main_menu(self):
        background_colour = BG_COLORS[16]
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        screen.fill(background_colour)
        pygame.display.flip()

        X = self.window_width
        Y = self.window_height
        screen = pygame.display.set_mode((X, Y))

    def add_new_number(self):
        empty_space = zip(*np.where(self.board_status == 0))
        empty_space = list(empty_space)

        for position in random.sample(empty_space, k=1):
            self.board_status[position] = 2

    def game_over_screen(self):
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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
                self.game_over_screen()
                self.play()

    def draw_board(self):
        self.start_time = 7
        self.window.fill(self.window_bg_color)
        pink_back = pygame.image.load("pink_back.png")
        image_end = pygame.transform.scale(pink_back, (self.window_width, self.window_height))
        self.window.blit(image_end, (0, 0))
        if self.game_over():
            self.game_over_screen()

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
                        BG_COLORS[cell_value],
                        pygame.Rect(rect_x, rect_y, self.cell_size, self.cell_size)
                    )

                    if cell_value != 0:
                        text_surface = self.myFont.render(f"{cell_value}", True, (0, 0, 0))
                        text_rect = text_surface.get_rect(center=(rect_x + self.block_size / 2, rect_y + self.block_size / 2))
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    running = False
                    self.game_over_screen()



if __name__ == "__main__":
    game = game_2048()
    game.intro()
    game.play()