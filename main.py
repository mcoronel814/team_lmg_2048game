import pygame
from sys import exit


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

    def side_panel(self):
        for box in range(self.board_length):
            surface = pygame.Surface((0, 0))
            self.window.blit(surface, (0, 0))

    def play(self):
        playing = True
        while playing:
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # KEYBOARD CONTROLS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        print("UP")
                    # block_gravity = -15
                    elif event.key == pygame.K_DOWN:
                        print("DOWN")
                    elif event.key == pygame.K_RIGHT:
                        print("RIGHT")
                    elif event.key == pygame.K_LEFT:
                        print("LEFT")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if up_rect.collidepoint(event.pos):
                        print("UP")
                    if down_rect.collidepoint(event.pos):
                        print("DOWN")
                    if right_rect.collidepoint(event.pos):
                        print("RIGHT")
                    if left_rect.collidepoint(event.pos):
                        print("LEFT")


if __name__ == "__main__":
    game = game_2048()
    game.play()