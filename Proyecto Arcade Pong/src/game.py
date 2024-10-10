# game.py

import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, BLACK
from src.ball import Ball
from src.paddle import Paddle
from src.scoreboard import Scoreboard
from src.menu import Menu  

class Game:
    def __init__(self, player1_name="Jugador 1", player2_name="Jugador 2"):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Establecer el título de la ventana con los nombres de los jugadores
        self.player1_name = player1_name
        self.player2_name = player2_name
        pygame.display.set_caption(f"Pong - {self.player1_name} vs {self.player2_name}")
        self.clock = pygame.time.Clock()
        self.hit_sound = pygame.mixer.Sound('assets/sounds/bounce-8111.mp3')
        self.score_sound = pygame.mixer.Sound('assets/sounds/goal-sfx-95846.mp3')
        self.start_sound = pygame.mixer.Sound('assets/sounds/game-start-6104.mp3')

        # Instanciar objetos del juego
        self.ball = Ball()
        self.paddle1 = Paddle(30, SCREEN_HEIGHT // 2 - 50)
        self.paddle2 = Paddle(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2 - 50)
        self.scoreboard = Scoreboard()
        self.menu = Menu() 
        self.running = True
        self.game_active = True

        

    def run(self):
        self.show_timer()  # Mostrar el cronómetro antes de comenzar la partida
        self.game_active = True  # Iniciar la partida después del cronómetro
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_active = not self.game_active  # Alternar el estado del juego

                    # Manejar selección del menú
                    if not self.game_active:
                        if event.key == pygame.K_UP:
                            self.menu.move(-1)
                        elif event.key == pygame.K_DOWN:
                            self.menu.move(1)
                        elif event.key == pygame.K_RETURN:
                            if self.menu.select() == 0:  # Reiniciar juego
                                self.reset_game()
                            elif self.menu.select() == 1:  # Salir del juego
                                self.running = False

            if self.game_active:
                self.update_game()
            else:
                self.menu.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)



    def update_game(self):
        # Actualizar objetos
        self.ball.update()
        self.paddle1.move(pygame.K_w, pygame.K_s)
        self.paddle2.move(pygame.K_UP, pygame.K_DOWN)

        if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
            self.hit_sound.play()
        
        # Verificar si la pelota ha pasado los bordes
        if self.ball.rect.left <= 0:  # Jugador 2 anota
            self.score_sound.play()
            self.scoreboard.update_score(2)
            self.ball.reset()  # Reiniciar la pelota
        elif self.ball.rect.right >= SCREEN_WIDTH:  # Jugador 1 anota
            self.score_sound.play()
            self.scoreboard.update_score(1)
            self.ball.reset()  # Reiniciar la pelota

        # Verificar colisiones con las paletas
        if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
            self.ball.speed_x *= -1
            self.ball.speed_y *= 1.1  # Incrementar velocidad en Y al rebotar

        # Verificar si hay un ganador
        winner = self.scoreboard.check_winner()
        if winner:
            self.game_active = False  # Detener el juego
            self.show_winner(winner)  # Mostrar el ganador

        # Dibujar en pantalla
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, WHITE, self.paddle1.rect)
        pygame.draw.rect(self.screen, WHITE, self.paddle2.rect)
        pygame.draw.ellipse(self.screen, WHITE, self.ball.rect)
        pygame.draw.aaline(self.screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
        
        # Dibujar el marcador
        self.scoreboard.draw(self.screen)



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_menu()  # Llama al método para mostrar el menú


    def show_menu(self):
        font = pygame.font.Font(None, 74)
        text_restart = font.render("Reiniciar", True, (255, 255, 255))
        text_exit = font.render("Salir", True, (255, 255, 255))
        self.screen.fill(BLACK)  # Limpiar pantalla
        self.screen.blit(text_restart, (SCREEN_WIDTH // 2 - text_restart.get_width() // 2, SCREEN_HEIGHT // 2 - text_restart.get_height() // 2 - 50))
        self.screen.blit(text_exit, (SCREEN_WIDTH // 2 - text_exit.get_width() // 2, SCREEN_HEIGHT // 2 - text_exit.get_height() // 2 + 50))
        pygame.display.flip()  # Actualizar pantalla

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Reiniciar el juego
                        self.reset_game()
                        waiting = False
                    elif event.key == pygame.K_q:  # Salir del juego
                        self.running = False
                        waiting = False


    def show_timer(self):
        font = pygame.font.Font(None, 74)  # Crea la fuente
        for i in range(3, 0, -1):  # Cuenta de 3 a 1
            self.screen.fill(BLACK)  # Limpia la pantalla
            timer_text = font.render(str(i), True, (255, 255, 255))
            self.screen.blit(timer_text, (SCREEN_WIDTH // 2 - timer_text.get_width() // 2, SCREEN_HEIGHT // 2 - timer_text.get_height() // 2))
            pygame.display.flip()  # Actualiza la pantalla
            pygame.time.delay(1000)  # Espera 1 segundo
        # Mostrar "¡Iniciar!" o similar al final
        self.screen.fill(BLACK)  # Limpia la pantalla
        start_text = font.render("¡Iniciar!", True, (255, 255, 255))
        self.screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()  # Actualiza la pantalla para mostrar "¡Iniciar!"
        pygame.time.delay(1000)  # Espera 1 segundo antes de iniciar el juego
        self.start_sound.play()

    def show_winner(self, winner):
        """Mostrar al ganador y luego el menú de reiniciar o salir."""
        font = pygame.font.Font(None, 74)
        self.screen.fill(BLACK)
        winner_text = font.render(f"{winner} ha ganado!", True, WHITE)
        self.screen.blit(winner_text, (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 2 - winner_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(3000)  # Pausa de 3 segundos antes de mostrar el menú

        # Mostrar el menú de opciones después de la pausa
        self.game_active = False  # Asegurarse de que el juego esté pausado
        waiting = True
        while waiting:
            self.menu.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.menu.move(-1)
                    elif event.key == pygame.K_DOWN:
                        self.menu.move(1)
                    elif event.key == pygame.K_RETURN:
                        selection = self.menu.select()
                        if selection == 0:  # Reiniciar juego
                            self.reset_game()
                            waiting = False
                        elif selection == 1:  # Salir del juego
                            self.running = False
                            waiting = False

    def reset_game(self):
    # Reiniciar el puntaje y el estado del juego
        self.scoreboard.player1_score = 0
        self.scoreboard.player2_score = 0
        self.ball.reset()  # Reiniciar la pelota
        self.show_timer()  # Mostrar el cronómetro antes de reanudar el juego
        self.game_active = True  # Reanudar el juego