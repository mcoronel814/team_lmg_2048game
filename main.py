import pygame
import random
import numpy as np

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

                pygame.draw.rect(
                    self.window,
                    (0, 0, 0),
                    pygame.Rect(rect_x, rect_y, self.cell_size, self.cell_size)
                )

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
                data = self.draw_board[:, idx]
            else:
                data = self.draw_board[idx, :]

            flip = False
            if dir in "RD":
                flip = True
                data = data[::-1]

            data = self.merge_numbers(data)
            data = data + (self.board_length - len(data)) * [0]

            if flip:
                data = data[::-1]

            if dir in "UD":
                self.draw_board[:, idx] = data
            else:
                self.draw_board[idx, :] = data

    def play(self):
        game_active = True
        playing = True
        while playing:
            self.draw_board()
            pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    pygame.quit()
                    exit()
                if game_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            print("UP")
                        elif event.key == pygame.K_DOWN:
                            print("DOWN")
                        elif event.key == pygame.K_RIGHT:
                            print("RIGHT")
                        elif event.key == pygame.K_LEFT:
                            print("LEFT")


if __name__ == "__main__":
    game = game_2048()
    game.play()
