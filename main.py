import pygame
from sys import exit


def display_time_spent():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    time_surf = test_font.render(f'{current_time}', False, (255, 255, 255))
    time_rect = time_surf.get_rect(center = (500, 100))
    screen.blit(time_surf, time_rect)


pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('LMGs 2048')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True
start_time = 0

#surface = pygame.Surface((700, 400))
#surface.fill('beige')
# pygame.draw.rect(screen, 'Pink',(600,200))
# block_a1 = pygame.draw.rect(screen, 'Pink',(600,200))
# block_a2
# block_a3
# block_a4
# block_b1
# block_b2
# block_b3
# block_b4
# block_c1
# block_c2
# block_c3
# block_c4
# block_d1
# block_d2
# block_d3
# block_d4
#score_surface = test_font.render("Score:", False, "brown")

up_button = pygame.image.load("up_key.png").convert_alpha()
up_arrow = pygame.transform.scale(up_button, (50, 50))
up_rect = up_arrow.get_rect(bottomright=(550, 250))

down_button = pygame.image.load("down_key.png").convert_alpha()
down_arrow = pygame.transform.scale(down_button, (50, 50))
down_rect = down_arrow.get_rect(bottomright=(550, 300))

right_button = pygame.image.load("right_key.png").convert_alpha()
right_arrow = pygame.transform.scale(right_button, (50, 50))
right_rect = right_arrow.get_rect(bottomright=(600, 300))

left_button = pygame.image.load("left_key.png").convert_alpha()
left_arrow = pygame.transform.scale(left_button, (50, 50))
left_rect = left_arrow.get_rect(bottomright=(500, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # KEYBOARD CONTROLS
        if game_active:
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

        # MOUSE CONTROLS
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(event.pos)
                if up_rect.collidepoint(mouse_pos):
                    print('up')
                if down_rect.collidepoint(mouse_pos):
                    print("down")
                if right_rect.collidepoint(mouse_pos):
                    print("right")
                if left_rect.collidepoint(mouse_pos):
                    print("left")
        # reintroduce to game with space
        # else:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
        # (new board)
            start_time = int(pygame.time.get_ticks() / 1000)

    # draw all our elements
    # update everything
    # screen.blit(surface,(0,0))
    if game_active:
        screen.blit(up_arrow, up_rect)
        screen.blit(down_arrow, down_rect)
        screen.blit(right_arrow, right_rect)
        screen.blit(left_arrow, left_rect)
        display_time_spent()
        #screen.blit(score_surface, (500, 50))
        #screen.blit(screen,(700,400))

    # COLLISIONS
        #if block.colliderect(full_board):
            # game_active = False
    # else:
        # screen.fill(yellow)
        # screen.blit(ending message,(center = (350, 200))
        # ending_message = test_font.render("Game Over :", False, "brown")

    pygame.display.update()
    clock.tick(40)

# class game_2048:
# def __init__(self):
# self.board_length = 4
# self.cell_size = 100
# self.gap = 5
# self.window_bg_color = (187, 173, 160)
# self.block_size = self.cell_size + self.gap * 2

# self.window_width = self.block_size * 6
# self.window_height = self.block_size * 4

# pygame.init()


# block_gravity = 0


# self.window = pygame.display.set_mode((self.window_width, self.window_height))

# def draw_board(self):
# self.window.fill(self.window_bg_color)

# for r in range(self.board_length):
# rect_y = self.block_size * r + self.gap
# for c in range(self.board_length):
# rect_x = self.block_size * c + self.gap

# pygame.draw.rect(
# self.window,
# (0, 0, 0),
# pygame.Rect(rect_x, rect_y, self.cell_size, self.cell_size)
#  )

# def play(self):
# playing = True
# while playing:
# self.draw_board()
# pygame.display.update()

# for event in pygame.event.get():
# if event.type == pygame.QUIT:
# playing = False

# up_button()
# pygame.display.update()

# KEYBOARD CONTROLS
# if event.type == pygame.KEYDOWN:
# if event.key == pygame.K_UP:
#  print("UP")
# block_gravity = -15
# elif event.key == pygame.K_DOWN:
# print("DOWN")
# elif event.key == pygame.K_RIGHT:
#   print("RIGHT")
# elif event.key == pygame.K_LEFT:
#  print("LEFT")

# if event.type == pygame.MOUSEMOTION:
# print(event.pos)

# if event.type == MOUSEBUTTONDOWN:
# mouse_pos = pygame.mouse.get_pos:

# if up_rect.collidepoint(mouse_pos):
# direction = "up"
# if down_rect.collidepoint(mouse_pos):
# direction = "down"
# if right_rect.collidepoint(mouse_pos):
# direction = "right"
# if left_rect.collidepoint(mouse_pos):
# direction = "left"

# if direction == "down":
# block_gravity +=


# if __name__ == "__main__":
# game = game_2048()
# game.play()
