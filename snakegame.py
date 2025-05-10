import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Snake settings
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def score_display(score):
    value = font.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def game_loop():
    game_exit = False
    while not game_exit:
        x = width // 2
        y = height // 2
        dx = 0
        dy = 0
        direction = 'RIGHT'

        snake_list = []
        length_of_snake = 1

        food_x = random.randrange(0, width - snake_block, snake_block)
        food_y = random.randrange(0, height - snake_block, snake_block)

        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and direction != 'RIGHT':
                        dx = -snake_block
                        dy = 0
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        dx = snake_block
                        dy = 0
                        direction = 'RIGHT'
                    elif event.key == pygame.K_UP and direction != 'DOWN':
                        dy = -snake_block
                        dx = 0
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        dy = snake_block
                        dx = 0
                        direction = 'DOWN'

            x += dx
            y += dy

            if x >= width or x < 0 or y >= height or y < 0:
                game_over = True

            screen.fill(blue)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

            snake_head = [x, y]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_over = True

            draw_snake(snake_list)
            score_display(length_of_snake - 1)
            pygame.display.update()

            if x == food_x and y == food_y:
                food_x = random.randrange(0, width - snake_block, snake_block)
                food_y = random.randrange(0, height - snake_block, snake_block)
                length_of_snake += 1

            clock.tick(snake_speed)

        # Game over screen
        while game_over and not game_exit:
            screen.fill(black)
            msg = font.render("Game Over! Press C to Play Again or Q to Quit", True, red)
            screen.blit(msg, [width // 6, height // 3])
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        game_over = False  # restart loop

    pygame.quit()
    quit()

game_loop()
