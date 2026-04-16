import pygame

class Ball:
    def __init__(self, x, y, radius=25, speed=20, screen_width=600, screen_height=400):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, dx, dy):
        # Calculate new position
        new_x = self.x + dx
        new_y = self.y + dy

        # Check left/right boundaries
        if new_x - self.radius >= 0 and new_x + self.radius <= self.screen_width:
            self.x = new_x

        # Check top/bottom boundaries
        if new_y - self.radius >= 0 and new_y + self.radius <= self.screen_height:
            self.y = new_y

    def draw(self, screen):
        # Draw red ball
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)