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
        "white": (214, 214, 214)

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
        self.myFont = pygame.font.SysFont("Comic Sans MS", 30)
        pygame.display.set_caption('2048 - brought to you by LMG')
        self.start_time = 0
        self.score = 0

        # start the board with zeros and random number
        self.board_status = np.zeros((self.board_length, self.board_length))
        self.add_new_number()

    def intro(self):
        background_colour = PINK[16]
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

        text_intro = self.myFont.render('2048 - brought to you by LMG', True, PINK[32], PINK[64])
        textRect = text_intro.get_rect()
        textRect.center = (X // 2, Y // 2)
        screen.blit(text_intro, textRect)
        pygame.display.flip()
        time.sleep(3)

    def main_menu(self):
        background_colour = PINK[16]
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        screen.fill(background_colour)
        pygame.display.flip()

        X = self.window_width
        Y = self.window_height
        screen = pygame.display.set_mode((X, Y))

        text_color = (PINK["white"])
        button_bg_color = (PINK[64])
        hover_color = (PINK[32])

        smallfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = smallfont.render('New Game', True, text_color)

        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if X / 2 <= mouse[0] <= X / 2 + 140 and Y / 2 <= mouse[1] <= Y / 2 + 40:
                        game = game_2048()
                        game.play()

            screen.fill((187, 173, 160))
            mouse = pygame.mouse.get_pos()

            if X / 2 <= mouse[0] <= X / 2 + 140 and Y / 2 <= mouse[1] <= Y / 2 + 40:
                pygame.draw.rect(screen, hover_color, [X / 2, Y / 2, 140, 40])
            else:
                pygame.draw.rect(screen, button_bg_color, [X / 2, Y / 2, 140, 40])

            screen.blit(text, (X / 2 + 50, Y / 2))
            pygame.display.update()

    def add_new_number(self):
        empty_space = zip(*np.where(self.board_status == 0))
        empty_space = list(empty_space)

        for position in random.sample(empty_space, k=1):
            self.board_status[position] = 2

    def draw_board(self):
        self.window.fill(self.window_bg_color)
        if self.game_over():
            self.window.fill("yellow")
            ending_message = self.myFont.render("Game Over !!!", False, "brown")
            self.window.blit(ending_message, (250, 200))
        else:
            up_button = pygame.image.load("up_key.png").convert_alpha()
            up_arrow = pygame.transform.scale(up_button, (50, 50))
            up_rect = up_arrow.get_rect(bottomright=(575, 325))

            down_button = pygame.image.load("down_key.png").convert_alpha()
            down_arrow = pygame.transform.scale(down_button, (50, 50))
            down_rect = down_arrow.get_rect(bottomright=(575, 380))

            right_button = pygame.image.load("right_key.png").convert_alpha()
            right_arrow = pygame.transform.scale(right_button, (50, 50))
            right_rect = right_arrow.get_rect(bottomright=(630, 380))

            left_button = pygame.image.load("left_key.png").convert_alpha()
            left_arrow = pygame.transform.scale(left_button, (50, 50))
            left_rect = left_arrow.get_rect(bottomright=(520, 380))

            current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
            time_surf = self.myFont.render(f'Time Played: {current_time}', False, (255, 255, 255))
            time_rect = time_surf.get_rect(center=(550, 100))

            score_surf = self.myFont.render(f'Score: {self.score}', False, (255, 255, 255))
            score_rect = score_surf.get_rect(topright=(600, 50))

            self.window.blit(up_arrow, up_rect)
            self.window.blit(down_arrow, down_rect)
            self.window.blit(right_arrow, right_rect)
            self.window.blit(left_arrow, left_rect)
            self.window.blit(time_surf, time_rect)
            self.window.blit(score_surf, score_rect)

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

                    if cell_value != 0:
                        text_surface = self.myFont.render(f"{cell_value}", True, PINK["white"])
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
                    up_button = pygame.image.load("up_key.png").convert_alpha()
                    up_arrow = pygame.transform.scale(up_button, (50, 50))
                    up_rect = up_arrow.get_rect(bottomright=(575, 325))

                    down_button = pygame.image.load("down_key.png").convert_alpha()
                    down_arrow = pygame.transform.scale(down_button, (50, 50))
                    down_rect = down_arrow.get_rect(bottomright=(575, 380))

                    right_button = pygame.image.load("right_key.png").convert_alpha()
                    right_arrow = pygame.transform.scale(right_button, (50, 50))
                    right_rect = right_arrow.get_rect(bottomright=(630, 380))

                    left_button = pygame.image.load("left_key.png").convert_alpha()
                    left_arrow = pygame.transform.scale(left_button, (50, 50))
                    left_rect = left_arrow.get_rect(bottomright=(520, 380))

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