import pygame

class game2048:
    def __init__(self):
        self.window_width = 600
        self.window_height = 750

        pygame.init()

        self.window = pygame.display.set_mode((self.window_width, self.window_height))

    def play(self):
        playing = True
        while playing:
            pygame.display.update()


if __name__ == "__main__":
    game = game2048()
    game.play()