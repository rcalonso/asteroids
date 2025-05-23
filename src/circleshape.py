from __future__ import annotations

import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        pass

    def update(self, dt: float):
        pass

    def collision(self, other: CircleShape) -> bool:
        distance = self.position.distance_to(other.position)
        if distance <= self.radius + other.radius:
            return True
        else:
            return False
