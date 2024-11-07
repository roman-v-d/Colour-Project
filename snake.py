import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen size and colors
screen_width = 600
screen_height = 400
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up display
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Game clock
clock = pygame.time.Clock()

# Snake properties
snake_block = 10
snake_speed = 15

# Font styles
font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 25)

# Score function
def score_display(score):
    value = score_font.render("Score: " + str(score), True, white)
    display.blit(value, [0, 0])

# Snake drawing function
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Message function
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [screen_width / 6, screen_height / 3])

# Game loop function
def game_loop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Movement variables
    x1_change = 0
    y1_change = 0

    # Snake attributes
    snake_list = []
    length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Key events for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Boundaries check
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        # Update position
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, white, [foodx, foody, snake_block, snake_block])
        
        # Snake head
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        # Check if snake has grown
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score_display(length_of_snake - 1)

        pygame.display.update()

        # Check if snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
game_loop()