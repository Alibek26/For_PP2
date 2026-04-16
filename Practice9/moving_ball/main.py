import pygame
from ball import Ball

def main():
    pygame.init()

    # Screen setup
    screen_width, screen_height = 600, 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Moving Red Ball")

    clock = pygame.time.Clock()

    # Create ball in center
    ball = Ball(
        x=screen_width // 2,
        y=screen_height // 2,
        screen_width=screen_width,
        screen_height=screen_height
    )

    running = True
    while running:
        screen.fill((255, 255, 255))  # white background

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Movement controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball.move(-ball.speed, 0)

                elif event.key == pygame.K_RIGHT:
                    ball.move(ball.speed, 0)

                elif event.key == pygame.K_UP:
                    ball.move(0, -ball.speed)

                elif event.key == pygame.K_DOWN:
                    ball.move(0, ball.speed)

        # Draw ball
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()