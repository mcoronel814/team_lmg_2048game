import pygame


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


    def play(self):
        playing = True
        while playing:
            self.draw_board()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False


if __name__ == "__main__":
    game = game_2048()
    game.play()
