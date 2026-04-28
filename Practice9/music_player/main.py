import pygame
import os
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(BASE_DIR, "music")

player = MusicPlayer(music_path)

running = True

def draw_ui():
    screen.fill((255, 255, 255))

    title = font.render("Music Player", True, (0, 0, 0))
    screen.blit(title, (200, 20))

    track = font.render(f"Track: {player.get_current_track_name()}", True, (0, 0, 0))
    screen.blit(track, (50, 100))

    # 🔥 прогресс бар
    progress = player.get_progress()

    bar_x, bar_y = 50, 150
    bar_width, bar_height = 500, 10

    pygame.draw.rect(screen, (200, 200, 200), (bar_x, bar_y, bar_width, bar_height))
    pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width * progress, bar_height))

    controls = font.render("P-Play S-Stop N-Next B-Back Q-Quit", True, (0, 0, 0))
    screen.blit(controls, (50, 200))

    pygame.display.flip()


while running:
    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.previous_track()
            elif event.key == pygame.K_q:
                running = False

    clock.tick(60)

pygame.quit()