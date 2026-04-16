import pygame
from player import MusicPlayer

def draw_text(screen, text, x, y, font):
    # Render and draw text on screen
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

def main():
    pygame.init()

    # Create window
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Music Player")

    # Font for UI text
    font = pygame.font.SysFont("Arial", 24)

    # Create music player instance
    player = MusicPlayer("music")

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((30, 30, 30))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                # Play music
                if event.key == pygame.K_p:
                    player.play()

                # Stop music
                elif event.key == pygame.K_s:
                    player.stop()

                # Next track
                elif event.key == pygame.K_n:
                    player.next_track()

                # Previous track
                elif event.key == pygame.K_b:
                    player.prev_track()

                # Quit program
                elif event.key == pygame.K_q:
                    running = False

        # UI display
        draw_text(screen, "Music Player", 20, 20, font)
        draw_text(screen, f"Track: {player.get_current_track()}", 20, 80, font)
        draw_text(screen, f"Status: {player.get_status()}", 20, 120, font)

        draw_text(screen, "Controls: P=Play | S=Stop | N=Next | B=Back | Q=Quit", 20, 200, font)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()