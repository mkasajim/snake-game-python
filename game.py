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
CELL_SIZE = 10
CELLS_WIDE = WINDOW_WIDTH // CELL_SIZE
CELLS_HIGH = WINDOW_HEIGHT // CELL_SIZE

# Snake variables
SNAKE_BODY = [(CELLS_WIDE//2, CELLS_HIGH//2), (CELLS_WIDE//2-1, CELLS_HIGH//2)] 
SNAKE_DIRECTION = 'right'
SNAKE_SPEED = 5

# Food variables
FOOD_POSITION = None
FOOD_COLOR = RED

# Score variables
score = 0
font = pygame.font.Font(None, 32)

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
            elif event.key == pygame.K_RIGHT and SNAKE_DIRECTION != 'left':
                SNAKE_DIRECTION = 'right'
            elif event.key == pygame.K_UP and SNAKE_DIRECTION != 'down':
                SNAKE_DIRECTION = 'up'
            elif event.key == pygame.K_DOWN and SNAKE_DIRECTION != 'up':
                SNAKE_DIRECTION = 'down'

    # Move snake  
    head = SNAKE_BODY[0]
    if SNAKE_DIRECTION == 'right':
        new_head = (head[0]+1, head[1])
    elif SNAKE_DIRECTION == 'left':
        new_head = (head[0]-1, head[1])
    elif SNAKE_DIRECTION == 'up':
        new_head = (head[0], head[1]-1)
    elif SNAKE_DIRECTION == 'down':
        new_head = (head[0], head[1]+1)

    # Wrap snake
    if new_head[0] < 0:
        new_head = (CELLS_WIDE-1, new_head[1])
    elif new_head[0] >= CELLS_WIDE:
        new_head = (0, new_head[1])
        
    if new_head[1] < 0:
        new_head = (new_head[0], CELLS_HIGH-1)
    elif new_head[1] >= CELLS_HIGH:
        new_head = (new_head[0], 0)

    # Grow snake  
    if new_head == FOOD_POSITION:
        score += 1
        FOOD_POSITION = None
        SNAKE_SPEED += 0.5 # Increase speed
    else:
        SNAKE_BODY.pop()
        
    SNAKE_BODY.insert(0, new_head)

    # Respawn food
    if FOOD_POSITION is None:
        while FOOD_POSITION is None or FOOD_POSITION in SNAKE_BODY:
            FOOD_POSITION = (random.randint(0, CELLS_WIDE-1), random.randint(0, CELLS_HIGH-1))

    # Game over
    if new_head in SNAKE_BODY[1:]:
        game_over = True
        print('Game over!')

    # Draw screen
    screen.fill(BLACK)
    
    score_text = font.render("Score: " + str(score), True, WHITE) 
    screen.blit(score_text, (WINDOW_WIDTH - 100, 10))
        
    for pos in SNAKE_BODY:
        pygame.draw.rect(screen, WHITE, pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)) 
    
    pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(FOOD_POSITION[0]*CELL_SIZE, FOOD_POSITION[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.update()
    clock.tick(SNAKE_SPEED) 

pygame.quit()
