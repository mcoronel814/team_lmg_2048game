import pygame
import random
import numpy as np

# Background color's dictionary goes here


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
            self.draw_board()
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

                    if self.game_over():
                        print("Game Over !!")
                        return

                    if (self.board_status == old_board_status).all() == False:
                        self.add_new_number()


if __name__ == "__main__":
    game = game_2048()
    game.play()
