import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT 

class Menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)
        self.title = self.font.render("Pong Game", True, (255, 255, 255))
        self.restart_text = self.font.render("Reiniciar", True, (255, 255, 255))
        self.exit_text = self.font.render("Salir", True, (255, 255, 255))
        self.active_option = 0

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Fondo negro
        screen.blit(self.title, (SCREEN_WIDTH // 2 - self.title.get_width() // 2, SCREEN_HEIGHT // 4))
        
        # Opciones
        restart_rect = self.restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        exit_rect = self.exit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        
        screen.blit(self.restart_text, restart_rect)
        screen.blit(self.exit_text, exit_rect)

        # Resaltar la opción activa
        if self.active_option == 0:
            pygame.draw.rect(screen, (255, 255, 0), restart_rect.inflate(20, 20), 3)  # Resaltar opción reiniciar
        else:
            pygame.draw.rect(screen, (255, 255, 0), exit_rect.inflate(20, 20), 3)  # Resaltar opción salir

    def move(self, direction):
        self.active_option += direction
        if self.active_option < 0:
            self.active_option = 1
        elif self.active_option > 1:
            self.active_option = 0

    def select(self):
        return self.active_option
