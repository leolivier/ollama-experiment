import pygame
import random
import time

pygame.init()

# Game window and settings
window_width = 400
window_height = 400
window_title = "Snake Game"

# Snake settings
snake_speed = 10
snake_color = (255, 0, 0)
snake_body_size = 10

# Food settings
food_color = (0, 255, 0)
food_size = 5

# Game loop
while True:
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption(window_title)

    # Draw snake
    snake_x = window_width // 2 - snake_body_size // 2
    snake_y = window_height // 2 - snake_body_size // 2
    snake_body = []
    for i in range(1, snake_body_size):
        x = snake_x - i * snake_body_size
        y = snake_y
        snake_body.append([x, y])

    # Draw food
    food_x = random.randint(0, window_width - food_size)
    food_y = random.randint(0, window_height - food_size)

    # Check for collision
    if snake_body == food_x and snake_body == food_y:
        snake_body_size += 1

    # Check for edge collision
    for x, y in snake_body:
        if x < 0 or x > window_width - snake_body_size or y < 0 or y > window_height - snake_body_size:
            pygame.quit()
            exit()

    # Move snake
    if len(snake_body) < window_width // 2:
        snake_x -= snake_speed
    elif len(snake_body) > window_width // 2:
        snake_x += snake_speed
    elif len(snake_body) < window_height // 2:
        snake_y -= snake_speed
    else:
        snake_y += snake_speed

    # Update snake body
    for i in range(1, len(snake_body)):
        snake_body[i] = snake_body[i - 1]
        snake_body[i] = snake_body[i - 1]

    # Draw game window
    window.fill((0, 0, 0))
    for x, y in snake_body:
        pygame.draw.rect(window, snake_color, (x, y, snake_body_size, snake_body_size))
    pygame.draw.rect(window, food_color, (food_x, food_y, food_size, food_size))
    pygame.display.flip()

    # Wait for 5 seconds before updating the game
    time.sleep(1)
