import pygame

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

current_color = BLACK  # текущий цвет

# Fill background with white
screen.fill(WHITE)

# Modes and state
mode = "draw"
drawing = False
start_pos = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Switch modes and colors
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_b:
                mode = "draw"

            # Color selection
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
            elif event.key == pygame.K_5:
                current_color = YELLOW

        # Mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Mouse button released
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            x1, y1 = start_pos
            x2, y2 = event.pos

            if mode == "rect":
                rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
                pygame.draw.rect(screen, current_color, rect, 2)

            elif mode == "circle":
                radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, (x1, y1), radius, 2)

    # Drawing while holding mouse button
    if drawing:
        mx, my = pygame.mouse.get_pos()

        if mode == "draw":
            pygame.draw.circle(screen, current_color, (mx, my), 3)

        elif mode == "eraser":
            pygame.draw.circle(screen, WHITE, (mx, my), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()