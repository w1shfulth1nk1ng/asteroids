import pygame

from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_RADIUS,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.player_radius = PLAYER_RADIUS
        self.line_width = LINE_WIDTH
        self.player_turn_speed = PLAYER_TURN_SPEED
        self.player_speed = PLAYER_SPEED
        self.player_shoot_speed = PLAYER_SHOOT_SPEED
        self.shot_radius = SHOT_RADIUS
        self.rotation = 0
        self.shoot_timer = 0
        self.player_shoot_cooldown_seconds = PLAYER_SHOOT_COOLDOWN_SECONDS

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.player_radius / 1.5
        )
        a = self.position + forward * self.player_radius
        b = self.position - forward * self.player_radius - right
        c = self.position - forward * self.player_radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), self.line_width)

    def rotate(self, dt):
        self.rotation += self.player_turn_speed * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        self.shoot_timer -= dt
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * self.player_speed * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shoot_timer > 0:
            return
        else:
            self.shoot_timer = self.player_shoot_cooldown_seconds
        shot = Shot(self.position.x, self.position.y, self.shot_radius)
        shot.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * self.player_shoot_speed
        )
