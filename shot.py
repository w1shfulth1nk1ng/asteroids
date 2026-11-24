import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.line_width = LINE_WIDTH

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, self.line_width)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
