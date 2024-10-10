import pygame
from src.settings import SCREEN_WIDTH
from src.settings import WHITE

class Scoreboard:
    def __init__(self, max_score=10):
        self.player1_score = 0
        self.player2_score = 0
        self.max_score = max_score

    def update_score(self, player):
        if player == 1:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def draw(self, screen):
        font = pygame.font.Font(None, 74)
        score_text = f"{self.player1_score} - {self.player2_score}"
        score_surface = font.render(score_text, True, WHITE)
        screen.blit(score_surface, (SCREEN_WIDTH // 2 - score_surface.get_width() // 2, 10))

    def check_winner(self):
        if self.player1_score >= self.max_score:
            return "Jugador 1"
        elif self.player2_score >= self.max_score:
            return "Jugador 2"
        return None

    def reset(self):  # Añadir este método
        self.player1_score = 0
        self.player2_score = 0


