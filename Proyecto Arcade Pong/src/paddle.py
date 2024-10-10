import pygame
from src.settings import SCREEN_HEIGHT

class Paddle:
    def __init__(self, x, y):
        self.image = pygame.Surface((10, 100))  # Tamaño de la paleta
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 10  # Velocidad inicial de la paleta (aumenta este valor)
        self

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed  # Mover hacia arriba
        if keys[down_key] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed  # Mover hacia abajo
