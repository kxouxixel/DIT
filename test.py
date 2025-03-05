import pygame
from random import randint

# Размеры окна
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Количество рядов и колонок блоков
BLOCK_ROWS = 8
BLOCK_COLS = 16

# Размеры блока
BLOCK_WIDTH = SCREEN_WIDTH // BLOCK_COLS
BLOCK_HEIGHT = 15

# Положение первой строки блоков
BLOCK_TOP_MARGIN = 50

# Параметры платформы
PLATFORM_WIDTH = 80
PLATFORM_HEIGHT = 12
PLATFORM_COLOR = GREEN

# Параметры шарика
BALL_RADIUS = 7
BALL_COLOR = WHITE
BALL_SPEED_X = 4
BALL_SPEED_Y = -4


# Класс блока
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_left(self):
        self.rect.x -= 5
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += 5
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


# Класс шарика
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отражение от стенок
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.reset()

    def reset(self):
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def collide_platform(self, platform):
        return pygame.sprite.collide_rect(self, platform)

    def collide_block(self, block):
        return pygame.sprite.collide_rect(self, block)


# Функция для создания уровня
def create_level():
    blocks = pygame.sprite.Group()
    colors = [RED, BLUE, YELLOW, PURPLE]
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            block_color = colors[row % len(colors)]
            block_x = col * BLOCK_WIDTH
            block_y = BLOCK_TOP_MARGIN + row * BLOCK_HEIGHT
            block = Block(block_x, block_y, BLOCK_WIDTH, BLOCK_HEIGHT, block_color)
            blocks.add(block)
    return blocks


# Основная функция игры
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Breakout')

    clock = pygame.time.Clock()

    # Создание объектов
    platform = Platform(SCREEN_WIDTH // 2 - PLATFORM_WIDTH // 2,
                        SCREEN_HEIGHT - PLATFORM_HEIGHT - 20,
                        PLATFORM_WIDTH, PLATFORM_HEIGHT, PLATFORM_COLOR)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS, BALL_COLOR)
    blocks = create_level()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(platform)
    all_sprites.add(ball)
    all_sprites.add(blocks)

    game_over = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            platform.move_left()
        elif keys[pygame.K_RIGHT]:
            platform.move_right()

        # Обновление состояния всех спрайтов
        all_sprites.update()

        # Проверка столкновений шара с платформой
        if ball.collide_platform(platform):
            ball.speed_y *= -1

        # Проверка столкновений шара с блоками
        hit_blocks = pygame.sprite.spritecollide(ball, blocks, True)
        for block in hit_blocks:
            ball.speed_y *= -1

        # Проверка окончания игры
        if not blocks and not game_over:
            font = pygame.font.Font(None, 36)
            text = font.render("You Win!", True, WHITE)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
            pygame.display.flip()
            game_over = True
            pygame.time.wait(3000)
            break

        # Отрисовка всех элементов
        screen.fill(BLACK)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()