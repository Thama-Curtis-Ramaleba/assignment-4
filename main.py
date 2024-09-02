import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('100m Sprint')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_pos = [50, SCREEN_HEIGHT - 60]
player_size = 50
player_speed = 5

# Game clock
clock = pygame.time.Clock()

# Font for displaying time
font = pygame.font.SysFont("Arial", 30)

# Timer and start flag
start_time = None
running = False

def game_over():
    screen.fill(WHITE)
    game_over_text = font.render("Finished!", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 20))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

def draw_player():
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

def display_time(time_elapsed):
    time_text = font.render(f"Time: {time_elapsed:.2f} seconds", True, BLACK)
    screen.blit(time_text, (10, 10))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[K_SPACE] and not running:
        start_time = pygame.time.get_ticks()
        running = True

    if running:
        player_pos[0] += player_speed
        
        if player_pos[0] >= SCREEN_WIDTH - player_size:
            time_elapsed = (pygame.time.get_ticks() - start_time) / 1000
            display_time(time_elapsed)
            game_over()
    
    screen.fill(WHITE)
    draw_player()
    
    if running and start_time:
        time_elapsed = (pygame.time.get_ticks() - start_time) / 1000
        display_time(time_elapsed)
    
    pygame.display.update()
    clock.tick(60)

