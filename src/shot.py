import pygame

from src.circleshape import CircleShape
from src.constants import SHOT_RADIUS


class Shot(CircleShape):
    containers = []

    def __init__(self, x: int, y: int):
        super().__init__(x, y, radius=SHOT_RADIUS)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            surface=screen,
            color=(255, 255, 255),
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt: float):
        self.position += self.velocity * dt
