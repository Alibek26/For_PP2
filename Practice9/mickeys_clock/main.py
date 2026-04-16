import pygame
from clock import MickeyClock

def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Mickey Clock")

    clock = pygame.time.Clock()
    mickey_clock = MickeyClock(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mickey_clock.update()

        screen.fill((255, 255, 255))
        mickey_clock.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    