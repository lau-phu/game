import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Snake Game")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Define font
font = pygame.font.SysFont(None, 30)

# Define variables
snake_speed = 10
snake_list = []
snake_length = 1
food_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
obstacle_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
lives = 3

# Define functions
def draw_snake(snake_list):
    for snake_pos in snake_list:
        pygame.draw.rect(screen, GREEN, [snake_pos[0], snake_pos[1], 10, 10])

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], 10, 10])

def draw_obstacle(obstacle_pos):
    pygame.draw.rect(screen, GREY, [obstacle_pos[0], obstacle_pos[1], 10, 10])

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [WIDTH/2, HEIGHT/2])

# Start game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_change = -10
        y_change = 0
    elif keys[pygame.K_RIGHT]:
        x_change = 10
        y_change = 0
    elif keys[pygame.K_UP]:
        x_change = 0
        y_change = -10
    elif keys[pygame.K_DOWN]:
        x_change = 0
        y_change = 10

    # Move snake
    snake_head = []
    snake_head.append(snake_list[-1][0] + x_change)
    snake_head.append(snake_list[-1][1] + y_change)
    snake_list.append(snake_head)

    # Check for collisions
    if snake_head == food_pos:
        food_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
        snake_length += 1

    if len(snake_list) > snake_length:
        del snake_list[0]

    if snake_head[0] < 0 or snake_head[0] > WIDTH-10 or snake_head[1] < 0 or snake_head[1] > HEIGHT-10:
        lives -= 1
        if lives == 0:
            game_over = True
        else:
            snake_list = []
            snake_length = 1

    if snake_head in snake_list[:-1]:
        lives -= 1
        if lives == 0:
            game_over = True
        else:
            snake