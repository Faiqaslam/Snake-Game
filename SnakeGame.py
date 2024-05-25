import pygame
import random

# Initialize pygame
pygame.init()

# Set up display dimensions
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake and food positions
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1
snake_head = [width / 2, height / 2]
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]

# Directions
direction = 'RIGHT'
change_to = direction

# Score
score = 0

# Function to draw snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, green, [block[0], block[1], snake_block, snake_block])

# Function to display message
def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

def gameLoop():
    global direction, change_to, food_pos 
    game_over = False
    game_close = False

    # Initialize snake
    direction = 'RIGHT'
    snake_head = [width / 2, height / 2]
    snake_list = []
    snake_length = 1

    while not game_over:

        while game_close == True:
            display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                elif event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'

        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        elif change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        elif change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        elif change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'

        if direction == 'LEFT':
            snake_head[0] -= snake_block
        elif direction == 'RIGHT':
            snake_head[0] += snake_block
        elif direction == 'UP':
            snake_head[1] -= snake_block
        elif direction == 'DOWN':
            snake_head[1] += snake_block

        # Check for collision with boundaries
        if snake_head[0] >= width or snake_head[0] < 0 or snake_head[1] >= height or snake_head[1] < 0:
            game_close = True
        # Check for collision with self
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Move snake
        snake_cur = []
        snake_cur.append(snake_head[0])
        snake_cur.append(snake_head[1])
        snake_list.append(snake_cur)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with food
        if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
            food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
            snake_length += 1

        display.fill(white)
        pygame.draw.rect(display, red, [food_pos[0], food_pos[1], snake_block, snake_block])
        draw_snake(snake_block, snake_list)

        pygame.display.update()

        # Set frame rate
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
