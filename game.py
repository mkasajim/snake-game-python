import pygame
import random
import sys

# Initialize pygame 
pygame.init()

# Set up game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game variables
CELL_SIZE = 30
CELLS_WIDE = WINDOW_WIDTH // CELL_SIZE
CELLS_HIGH = WINDOW_HEIGHT // CELL_SIZE

# Snake variables
SNAKE_SPEED = CELL_SIZE
SNAKE_BODY = [(CELLS_WIDE//2, CELLS_HIGH//2)]
SNAKE_DIRECTION = 'right'

# Food variables
FOOD_POSITION = (random.randint(0, CELLS_WIDE-1), random.randint(0, CELLS_HIGH-1))
FOOD_COLOR = RED

# Game loop
clock = pygame.time.Clock()
game_over = False
while not game_over:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and SNAKE_DIRECTION != 'right':
                SNAKE_DIRECTION = 'left'  
            if event.key == pygame.K_RIGHT and SNAKE_DIRECTION != 'left':
                SNAKE_DIRECTION = 'right'
            if event.key == pygame.K_UP and SNAKE_DIRECTION != 'down':
                SNAKE_DIRECTION = 'up'
            if event.key == pygame.K_DOWN and SNAKE_DIRECTION != 'up':
                SNAKE_DIRECTION = 'down'

    # Move snake in direction
    if SNAKE_DIRECTION == 'right':
        snake_head = (SNAKE_BODY[0][0] + 1, SNAKE_BODY[0][1])
    if SNAKE_DIRECTION == 'left':
        snake_head = (SNAKE_BODY[0][0] - 1, SNAKE_BODY[0][1]) 
    if SNAKE_DIRECTION == 'up':
        snake_head = (SNAKE_BODY[0][0], SNAKE_BODY[0][1] - 1)
    if SNAKE_DIRECTION == 'down':
        snake_head = (SNAKE_BODY[0][0], SNAKE_BODY[0][1] + 1)
        
    # Grow snake if food eaten
    if snake_head == FOOD_POSITION:
        FOOD_POSITION = (random.randint(0, CELLS_WIDE-1), random.randint(0, CELLS_HIGH-1)) 
    else:
        SNAKE_BODY.pop()
        
    SNAKE_BODY.insert(0, snake_head)
    
    # Game over conditions
    if (snake_head[0] < 0 or snake_head[0] >= CELLS_WIDE or 
        snake_head[1] < 0 or snake_head[1] >= CELLS_HIGH or
        snake_head in SNAKE_BODY[:-1]):
        game_over = True
        print('Game Over!')
        
    # Draw background
    screen.fill(BLACK)
    
    # Draw food
    pygame.draw.rect(screen, FOOD_COLOR, 
                    [FOOD_POSITION[0]*CELL_SIZE, FOOD_POSITION[1]*CELL_SIZE, 
                    CELL_SIZE, CELL_SIZE]) 
    
    # Draw snake
    for pos in SNAKE_BODY:
        pygame.draw.rect(screen, WHITE, 
                        [pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, 
                        CELL_SIZE, CELL_SIZE])
        
    # Update display and clock    
    pygame.display.update()
    clock.tick(SNAKE_SPEED) 

pygame.quit()
