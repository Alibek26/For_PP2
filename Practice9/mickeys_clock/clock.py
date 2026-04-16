import pygame
import datetime
import math

class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (300, 300)

        # background
        self.bg = pygame.image.load("images/mickey_hand.png").convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (600, 600))

    def get_time(self):
        now = datetime.datetime.now()
        return now.hour, now.minute, now.second

    def calculate_angles(self, hours, minutes, seconds):
        hour_angle = (hours % 12 + minutes / 60) * 30
        minute_angle = (minutes + seconds / 60) * 6
        second_angle = seconds * 6
        return hour_angle, minute_angle, second_angle

    def draw_hand(self, angle, length, color, width):
        rad = math.radians(angle - 90)

        x = self.center[0] + length * math.cos(rad)
        y = self.center[1] + length * math.sin(rad)

        pygame.draw.line(self.screen, color, self.center, (x, y), width)

    def update(self):
        self.hours, self.minutes, self.seconds = self.get_time()

        self.hour_angle, self.minute_angle, self.second_angle = self.calculate_angles(
            self.hours, self.minutes, self.seconds
        )

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

        # hour hand
        self.draw_hand(self.hour_angle, 120, (0, 0, 0), 8)

        # minute hand
        self.draw_hand(self.minute_angle, 180, (0, 0, 0), 6)

        # second hand
        self.draw_hand(self.second_angle, 200, (255, 0, 0), 3)