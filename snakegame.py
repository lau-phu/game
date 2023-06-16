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
YELLOW = (255, 255, 0)

# Define font
font = pygame.font.SysFont(None, 30)

# Define variables
snake_speed = 10
snake_list = []
snake_length = 1
food_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
obstacle_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
lives = 3
walls = []
super_food_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
super_food_timer = 0
super_food_active = False
score = 0
score_decay_timer = 0

# Define functions
def draw_snake(snake_list):
    for snake_pos in snake_list:
        pygame.draw.rect(screen, GREEN, [snake_pos[0], snake_pos[1], 10, 10])

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, [food_pos[0], food_pos[1], 10, 10])

def draw_obstacle(obstacle_pos):
    pygame.draw.rect(screen, GREY, [obstacle_pos[0], obstacle_pos[1], 10, 10])

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, BLUE, [wall[0], wall[1], 10, 10])

def draw_super_food(super_food_pos):
    pygame.draw.rect(screen, YELLOW, [super_food_pos[0], super_food_pos[1], 10, 10])

def draw_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

def draw_lives(lives):
    lives_text = font.render("Lives: " + str(lives), True, WHITE)
    screen.blit(lives_text, [WIDTH - 70, 10])

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
        score += 1

        # Randomly change walls
        for i in range(3):
            wall_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
            while wall_pos in walls or wall_pos == food_pos or wall_pos == obstacle_pos or wall_pos == snake_head or wall_pos in snake_list[:-1]:
                wall_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
            walls.append(wall_pos)

    if snake_head == super_food_pos:
        super_food_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
        super_food_timer = 0
        super_food_active = True
        snake_speed += 2

    if super_food_active:
        super_food_timer += 1
        if super_food_timer >= 120:  # Super food disappears after 2 seconds
            super_food_active = False
            snake_speed -= 2

    if snake_head[0] >= WIDTH or snake_head[0] < 0 or snake_head[1] >= HEIGHT or snake_head[1] < 0:
        lives -= 1
        if lives == 0:
            game_over = True
        else:
            snake_list.clear()
            snake_length = 1
            snake_speed = 10
            score_decay_timer = 0
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Complicated Snake Game")

    if snake_head in snake_list[:-1] or snake_head in walls:
        lives -= 1
        if lives == 0:
            game_over = True
        else:
            snake_list.clear()
            snake_length = 1
            snake_speed = 10
            score_decay_timer = 0
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Complicated Snake Game")

    if score_decay_timer >= 180:  # Score decays if not eating for longer than 3 seconds
        score = max(0, score - 1)
        score_decay_timer = 0
    else:
        score_decay_timer += 1

    if len(snake_list) >= (WIDTH // 10) * (HEIGHT // 10) // 2:
        WIDTH *= 2
        HEIGHT *= 2
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Complicated Snake Game")

    if len(snake_list) > snake_length:
        del snake_list[0]

    screen.fill(BLACK)
    draw_snake(snake_list)
    draw_food(food_pos)
    draw_obstacle(obstacle_pos)
    draw_walls(walls)
    if super_food_active:
        draw_super_food(super_food_pos)
    draw_score(score)
    draw_lives(lives)

    pygame.display.update()
    clock.tick(snake_speed)

# Quit the game
pygame.quit()