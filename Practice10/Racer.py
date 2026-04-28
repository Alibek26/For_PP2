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
coins_collected = 0
font = pygame.font.SysFont(None, 36)

# Difficulty
enemy_speed = 5

# Draw car
def draw_car(x, y, color):
    pygame.draw.rect(screen, color, (x, y, 50, 100), border_radius=10)
    pygame.draw.rect(screen, (200, 230, 255), (x+10, y+10, 30, 20), border_radius=5)
    pygame.draw.rect(screen, (200, 230, 255), (x+10, y+70, 30, 20), border_radius=5)
    pygame.draw.rect(screen, (20, 20, 20), (x-5, y+10, 5, 20))
    pygame.draw.rect(screen, (20, 20, 20), (x+50, y+10, 5, 20))
    pygame.draw.rect(screen, (20, 20, 20), (x-5, y+70, 5, 20))
    pygame.draw.rect(screen, (20, 20, 20), (x+50, y+70, 5, 20))

def spawn_enemy():
    lane = random.choice([WIDTH//2 - 80, WIDTH//2 + 30])
    enemies.append([lane, -100])

def spawn_coin():
    lane = random.choice([WIDTH//2 - 80, WIDTH//2 + 30])
    coins.append([lane + 15, -50])

running = True
enemy_timer = 0
coin_timer = 0

while running:
    screen.fill((150, 150, 150))

    # Score increases over time
    score += 0.05

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

    player_x = max(80, min(WIDTH - 130, player_x))

    # Road lines
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
        enemy[1] += enemy_speed
        enemy_rect = pygame.Rect(enemy[0], enemy[1], 50, 100)

        draw_car(enemy[0], enemy[1], (255, 0, 0))

        if player_rect.colliderect(enemy_rect):
            print("Game Over")
            running = False

        elif enemy[1] > HEIGHT:
            enemies.remove(enemy)

    # Coins
    for coin in coins[:]:
        coin[1] += 5
        pygame.draw.circle(screen, (255, 215, 0), (coin[0], coin[1]), 10)

        coin_rect = pygame.Rect(coin[0]-10, coin[1]-10, 20, 20)

        if player_rect.colliderect(coin_rect):
            coins.remove(coin)
            coins_collected += 1
            score += 5   # бонус за монету

        elif coin[1] > HEIGHT:
            coins.remove(coin)

    # Increase difficulty
    if int(score) % 20 == 0:
        enemy_speed = min(15, enemy_speed + 0.04)

    # Display score
    text1 = font.render(f"Score: {int(score)}", True, (0,0,0))
    text2 = font.render(f"Coins: {coins_collected}", True, (0,0,0))

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()