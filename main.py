import pygame
import random
import time
import numpy as np

# Background color's dictionary goes here
BG_COLORS = {
    0: (255,255,255),
    2: (255, 215, 157),
    4: (217, 2, 238),
    8: (241, 98, 255),
    16: (50, 13, 62),
    32: (255, 223, 177),
    64: (232, 13, 253),
    128: (246, 149, 255),
    256: (101,26, 125),
    512: (255, 229, 193),
    1024: (228,2,249),
    2048: (248,175,255)
}

class game_2048:
    def __init__(self):
        self.board_length = 4
        self.cell_size = 100
        self.gap = 5
        self.window_bg_color = (187, 173, 160)
        self.block_size = self.cell_size + self.gap * 2

        self.window_width = self.block_size * 6
        self.window_height = self.block_size * 4

        pygame.init()

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.myFont = pygame.font.SysFont("Comic Sans MS", 30)
        pygame.display.set_caption('2048 - brought to you by LMG')

        # start the board with zeros and random number
        self.board_status = np.zeros((self.board_length, self.board_length))
        self.add_new_number()

    def intro(self):
        background_colour = BG_COLORS[16]
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        screen.fill(background_colour)
        pygame.display.flip()
        time.sleep(1)
        text_intro = self.myFont.render('2048 - brought to you by LMG', True, BG_COLORS[32], BG_COLORS[64])
        textRect = text_intro.get_rect()
        X = self.window_width
        Y = self.window_height
        textRect.center = (X // 2, Y // 2)
        display_surface = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('2048 - brought to you by LMG')
        display_surface.blit(text_intro, textRect)
        #running = True
        #while running:
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #running = False

        logo57 = pygame.image.load("LMG_Logo_57.png").convert_alpha()
        logo_scale = pygame.transform.scale(logo57, (X, Y))
        logo_rect = logo_scale.get_rect(bottomright=(X // 2, Y // 2))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(5)

    def add_new_number(self):
        empty_space = zip(*np.where(self.board_status == 0))
        empty_space = list(empty_space)

        for position in random.sample(empty_space, k=1):
            self.board_status[position] = 2

    def draw_board(self):
        self.window.fill(self.window_bg_color)

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

    def side_panel(self):
        for box in range(self.board_length):
            surface = pygame.Surface((0, 0))
            self.window.blit(surface, (0, 0))


    def merge_numbers(self, data):
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

    def movement(self, dir):
        for idx in range(self.board_length):

            if dir in "UD":
                data = self.board_status[:, idx]
            else:
                data = self.board_status[idx, :]

            flip = False
            if dir in "RD":
                flip = True
                data = data[::-1]

            data = self.merge_numbers(data)
            data = data + (self.board_length - len(data)) * [0]

            if flip:
                data = data[::-1]

            if dir in "UD":
                self.board_status[:, idx] = data
            else:
                self.board_status[idx, :] = data

    def game_over(self):
        board_status_backup = self.board_status.copy()
        for dir in "UDLR":
            self.movement(dir)

            if (self.board_status == board_status_backup).all() == False:
                self.board_status = board_status_backup
                return False
        return True

    def play(self):
        running = True
        while running:
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

            self.draw_board()
            self.window.blit(up_arrow, up_rect)
            self.window.blit(down_arrow, down_rect)
            self.window.blit(right_arrow, right_rect)
            self.window.blit(left_arrow, left_rect)

            pygame.display.update()

            for event in pygame.event.get():
                old_board_status = self.board_status.copy()

                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # print("U")
                        self.movement("U")
                    elif event.key == pygame.K_DOWN:
                        # print("D")
                        self.movement("D")
                    elif event.key == pygame.K_LEFT:
                        # print("L")
                        self.movement("L")
                    elif event.key == pygame.K_RIGHT:
                        # print("R")
                        self.movement("R")
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if up_rect.collidepoint(event.pos):
                        self.movement("U")
                    if down_rect.collidepoint(event.pos):
                        self.movement("D")
                    if right_rect.collidepoint(event.pos):
                        self.movement("R")
                    if left_rect.collidepoint(event.pos):
                        self.movement("L")
                if self.game_over():
                    print("Game Over !!")
                    return
                if (self.board_status == old_board_status).all() == False:
                    self.add_new_number()


if __name__ == "__main__":
    game = game_2048()
    game.intro()
    game.play()
