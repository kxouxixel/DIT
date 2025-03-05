import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
background = pygame.image.load("background1.png")

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 10
        self.color = WHITE
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])
    
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.speed_y *= -1
            
        if self.x < 0 or self.x > WIDTH:
            return True
        return False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

class Paddle:
    def __init__(self, x, y, width, height, color=WHITE):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.score = 0
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

def display_score(score_left, score_right):
    font = pygame.font.Font(None, 36)
    text_left = font.render(f"{score_left}", True, WHITE)
    text_right = font.render(f"{score_right}", True, WHITE)
    screen.blit(text_left, (WIDTH//4, 20))
    screen.blit(text_right, (WIDTH*3//4, 20))

ball = Ball()
paddle_left = Paddle(30, HEIGHT//2 - 50, 10, 100)
paddle_right = Paddle(WIDTH - 40, HEIGHT//2 - 50, 10, 100)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        paddle_left.y -= 5
    elif keys[pygame.K_s]:
        paddle_left.y += 5
    
    if keys[pygame.K_UP]:
        paddle_right.y -= 5
    elif keys[pygame.K_DOWN]:
        paddle_right.y += 5
    
    
    if paddle_left.y < 0:
        paddle_left.y = 0
    elif paddle_left.y + paddle_left.height > HEIGHT:
        paddle_left.y = HEIGHT - paddle_left.height
        
        
    if paddle_right.y < 0:
        paddle_right.y = 0
    elif paddle_right.y + paddle_right.height > HEIGHT:
        paddle_right.y = HEIGHT - paddle_right.height
        
    game_over = ball.update()
    
    if ball.x - ball.radius <= paddle_left.x + paddle_left.width and \
       ball.y >= paddle_left.y and ball.y <= paddle_left.y + paddle_left.height:
        ball.speed_x *= -1
    elif ball.x + ball.radius >= paddle_right.x and \
         ball.y >= paddle_right.y and ball.y <= paddle_right.y + paddle_right.height:
        ball.speed_x *= -1
        
    if game_over:
        if ball.x < 0:
            paddle_right.score += 1
        else:
            paddle_left.score += 1
        ball = Ball()
    
    screen.blit(background, (0, 0))
    ball.draw(screen)
    paddle_left.draw(screen)
    paddle_right.draw(screen)
    
    display_score(paddle_left.score, paddle_right.score)
    
    pygame.display.update()