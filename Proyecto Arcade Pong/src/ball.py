import pygame
import random
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Ball:
    def __init__(self):
        self.image = pygame.Surface((25, 25))  # Aumentar el tamaño a 25x25
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed_x = 5  # Velocidad inicial en X
        self.speed_y = 5  # Velocidad inicial en Y
        self.base_speed = 5  # Velocidad base

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Verificar colisión con los bordes
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

    def reset(self):
        # Reiniciar la posición de la pelota
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # Asignar dirección aleatoria
        self.speed_x = self.base_speed * random.choice([-1, 1])  # Direcciones aleatorias en X
        self.speed_y = self.base_speed * random.choice([-1, 1])  # Direcciones aleatorias en Y
