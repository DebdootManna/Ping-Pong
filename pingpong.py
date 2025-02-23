import pygame
import pandas as pd
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BALL_SPEED = [5, 5]
PADDLE_SPEED = 7
SCORE_FILE = "score.csv"

# Colors and Fonts
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
font = pygame.font.Font(None, 50)
title_font = pygame.font.Font(None, 70)
score_font = pygame.font.Font(None, 40)

# Sounds
bounce_sound = pygame.mixer.Sound("Bounce.mp3")
score_sound = pygame.mixer.Sound("Score.mp3")

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

# Game mode selection
play_with_bot = False

# Class for Paddle
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 100)

    def move(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up] and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if keys[down] and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED

    def ai_move(self, ball):
        if ball.rect.centery > self.rect.centery:
            self.rect.y += PADDLE_SPEED
        elif ball.rect.centery < self.rect.centery:
            self.rect.y -= PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Class for Ball
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.speed = BALL_SPEED.copy()

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            bounce_sound.play()

        if self.rect.colliderect(left_paddle.rect) or self.rect.colliderect(right_paddle.rect):
            self.speed[0] = -self.speed[0] * 1.1
            bounce_sound.play()

        if self.rect.left <= 0:
            update_score(1)
            self.reset()
        elif self.rect.right >= WIDTH:
            update_score(0)
            self.reset()

    def reset(self):
        self.rect.x, self.rect.y = WIDTH // 2, HEIGHT // 2
        self.speed = BALL_SPEED.copy()

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

# Function to update score
def update_score(player):
    try:
        df = pd.read_csv(SCORE_FILE)
        scores = [df.iloc[0, 0], df.iloc[0, 1]]
    except (FileNotFoundError, pd.errors.EmptyDataError):
        scores = [0, 0]

    scores[player] += 1
    df = pd.DataFrame({"Player 1": [scores[0]], "Player 2": [scores[1]]})
    df.to_csv(SCORE_FILE, index=False)
    score_sound.play()

# Function to show landing screen
def show_landing_screen():
    global play_with_bot
    running = True

    while running:
        screen.fill(BLACK)
        title_text = title_font.render("PING PONG", True, WHITE)
        pvp_text = font.render("1. 2 Players", True, RED)
        bot_text = font.render("2. Play with Bot", True, BLUE)
        exit_text = font.render("3. Exit", True, WHITE)

        screen.blit(title_text, (WIDTH // 2 - 140, 100))
        screen.blit(pvp_text, (WIDTH // 2 - 100, 250))
        screen.blit(bot_text, (WIDTH // 2 - 100, 300))
        screen.blit(exit_text, (WIDTH // 2 - 100, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    play_with_bot = False
                    running = False
                elif event.key == pygame.K_2:
                    play_with_bot = True
                    running = False
                elif event.key == pygame.K_3:
                    pygame.quit()
                    exit()

# Show the landing screen
show_landing_screen()

# Create paddles and ball
left_paddle = Paddle(30, HEIGHT // 2 - 50)
right_paddle = Paddle(WIDTH - 50, HEIGHT // 2 - 50)
ball = Ball(WIDTH // 2, HEIGHT // 2)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    left_paddle.move(pygame.K_w, pygame.K_s)
    if play_with_bot:
        right_paddle.ai_move(ball)
    else:
        right_paddle.move(pygame.K_UP, pygame.K_DOWN)

    ball.move()

    # Draw everything
    left_paddle.draw()
    right_paddle.draw()
    ball.draw()

    # Display live score
    try:
        df = pd.read_csv(SCORE_FILE)
        scores = [df.iloc[0, 0], df.iloc[0, 1]]
    except (FileNotFoundError, pd.errors.EmptyDataError):
        scores = [0, 0]

    score_display = score_font.render(f"Player 1: {scores[0]}  |  Player 2: {scores[1]}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 150, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
