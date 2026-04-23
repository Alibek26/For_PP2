import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Snake initial state
snake = [(100, 100)]
dx, dy = 10, 0

# Game variables
score = 0
level = 1
speed = 10

# Font for UI
font = pygame.font.SysFont(None, 30)

# Function to spawn food (not on snake)
def spawn_food():
    while True:
        x = random.randrange(0, WIDTH, 10)
        y = random.randrange(0, HEIGHT, 10)
        if (x, y) not in snake:
            return x, y

food = spawn_food()

running = True

while running:
    screen.fill((0, 0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control snake direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dx, dy = 0, -10
    if keys[pygame.K_DOWN]:
        dx, dy = 0, 10
    if keys[pygame.K_LEFT]:
        dx, dy = -10, 0
    if keys[pygame.K_RIGHT]:
        dx, dy = 10, 0

    # Move snake head
    head = (snake[0][0] + dx, snake[0][1] + dy)

    # Check wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    snake.insert(0, head)

    # Check if food is eaten
    if head == food:
        score += 1
        food = spawn_food()

        # Increase level and speed every 3 points
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))

    # Draw food
    pygame.draw.rect(screen, (255, 0, 0), (*food, 10, 10))

    # Draw score and level
    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10,10))
    screen.blit(font.render(f"Level: {level}", True, (255,255,255)), (10,40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()