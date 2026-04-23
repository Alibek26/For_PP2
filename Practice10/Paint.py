import pygame

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# Default drawing color and mode
color = (0, 0, 0)
mode = "draw"

drawing = False
start_pos = (0, 0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Switch modes with keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"   # rectangle mode
            elif event.key == pygame.K_c:
                mode = "circle" # circle mode
            elif event.key == pygame.K_e:
                mode = "eraser" # eraser mode
            elif event.key == pygame.K_b:
                mode = "draw"   # free draw mode

        # Mouse pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Mouse released
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            # Draw rectangle
            if mode == "rect":
                x, y = start_pos
                w = event.pos[0] - x
                h = event.pos[1] - y
                pygame.draw.rect(screen, color, (x, y, w, h), 2)

            # Draw circle
            if mode == "circle":
                x, y = start_pos
                r = int(((event.pos[0]-x)**2 + (event.pos[1]-y)**2)**0.5)
                pygame.draw.circle(screen, color, (x, y), r, 2)

    # While holding mouse button
    if drawing:
        mx, my = pygame.mouse.get_pos()

        # Free drawing
        if mode == "draw":
            pygame.draw.circle(screen, color, (mx, my), 3)

        # Eraser (draw with white color)
        if mode == "eraser":
            pygame.draw.circle(screen, (255,255,255), (mx, my), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()