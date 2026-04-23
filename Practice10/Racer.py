import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# Player settings
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 120
player_speed = 6

# Enemies and coins
enemies = []
coins = []

# Road lines
lines = []
for i in range(10):
    lines.append([WIDTH//2 - 5, i * 60])

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Draw car (top view)
def draw_car(x, y, color):
    pygame.draw.rect(screen, color, (x, y, 50, 100), border_radius=10)
    pygame.draw.rect(screen, (200, 230, 255), (x+10, y+10, 30, 20), border_radius=5)
    pygame.draw.rect(screen, (200, 230, 255), (x+10, y+70, 30, 20), border_radius=5)
    pygame.draw.rect(screen, (20, 20, 20), (x-5, y+10, 5, 20))
    pygame.draw.rect(screen, (20, 20, 20), (x+50, y+10, 5, 20))
    pygame.draw.rect(screen, (20, 20, 20), (x-5, y+70, 5, 20))
    pygame.draw.rect(screen, (20, 20, 20), (x+50, y+70, 5, 20))

# Spawn enemy in lanes
def spawn_enemy():
    lane = random.choice([WIDTH//2 - 80, WIDTH//2 + 30])
    enemies.append([lane, -100])

# Spawn coin
def spawn_coin():
    lane = random.choice([WIDTH//2 - 80, WIDTH//2 + 30])
    coins.append([lane + 15, -50])  # center coin

running = True
enemy_timer = 0
coin_timer = 0

while running:
    screen.fill((150, 150, 150))  # road

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Limit movement
    player_x = max(80, min(WIDTH - 130, player_x))

    # Draw road lines
    for line in lines:
        pygame.draw.rect(screen, (255,255,255), (line[0], line[1], 10, 40))
        line[1] += 5
        if line[1] > HEIGHT:
            line[1] = -40

    # Spawn enemies
    enemy_timer += 1
    if enemy_timer > 60:
        spawn_enemy()
        enemy_timer = 0

    # Spawn coins
    coin_timer += 1
    if coin_timer > 90:
        spawn_coin()
        coin_timer = 0

    # Player
    player_rect = pygame.Rect(player_x, player_y, 50, 100)
    draw_car(player_x, player_y, (0, 150, 255))

    # Enemies
    for enemy in enemies[:]:
        enemy[1] += 6
        enemy_rect = pygame.Rect(enemy[0], enemy[1], 50, 100)

        draw_car(enemy[0], enemy[1], (255, 0, 0))

        # Collision with car
        if player_rect.colliderect(enemy_rect):
            print("Game Over")
            running = False

        elif enemy[1] > HEIGHT:
            enemies.remove(enemy)

    # Coins
    for coin in coins[:]:
        coin[1] += 5

        # Draw coin (circle)
        pygame.draw.circle(screen, (255, 215, 0), (coin[0], coin[1]), 10)

        coin_rect = pygame.Rect(coin[0]-10, coin[1]-10, 20, 20)

        # Collect coin
        if player_rect.colliderect(coin_rect):
            coins.remove(coin)
            score += 1

        elif coin[1] > HEIGHT:
            coins.remove(coin)

    # Score display (top-right)
    text = font.render(f"Coins: {score}", True, (0,0,0))
    screen.blit(text, (250, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()