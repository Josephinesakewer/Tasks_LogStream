import pygame
from random import randrange

pygame.init()

# Настройки экрана и игрового поля
width, height = 640, 660
size = 20
bg = pygame.image.load('C:\\Users\\Professional\\Desktop\\Courses logstream\\Задание 5\\2 часть. 3 вариант\\space.jpg')  # Замените 'space.jpg' на путь к вашему изображению
x, y = randrange(100, width - 100, size), randrange(100, height - 100, size)
Shroom = randrange(20, width - 20, size), randrange(40, height - 20, size)
Mushroom = pygame.image.load('C:\\Users\\Professional\\Desktop\\Courses logstream\\Задание 5\\2 часть. 3 вариант\\apple.png')  # Замените на ваше изображение гриба

# Настройки кнопок, змеи, очков, скорости и начальных координат
buttons = {'w': True, 's': True, 'a': True, 'd': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5
score = 0

# Настройки экрана и шрифтов
sc = pygame.display.set_mode([width, height])
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
Score_font = pygame.font.SysFont('Comic Sans MS', 32, bold=True)  # Новый шрифт и размер
game_over_font = pygame.font.SysFont('Comic Sans MS', 65, bold=True)

# Основной игровой цикл
while True:
    sc.blit(bg, (0, 0))  # Установка фона изображения
    [(pygame.draw.rect(sc, pygame.Color('purple'), (i, j, size - 2, size - 2))) for i, j in snake]  # Цвет змеи

    sc.blit(Mushroom, (*Shroom, size, size))
    score_render = Score_font.render(f'SCORE: {score}', 1, pygame.Color('yellow'))  # Цвет текста счета
    sc.blit(score_render, (10, 10))

    # Обновление координат змеи
    x += dx * size
    y += dy * size
    snake.append((x, y))
    snake = snake[-length:]

    # Проверка на съедение гриба
    if snake[-1] == Shroom:
        Shroom = randrange(20, width - 20, size), randrange(40, height - 20, size)
        length += 1
        score += 1
        fps += 1

    # Новое условие поражения (изменение границ и самопересечение)
    if x < 20 or x > (width - 40) or y < 40 or y > (height - 40) or len(snake) != len(set(snake)):
        while True:
            game_over = game_over_font.render('GAME OVER', 1, pygame.Color('red'))
            sc.blit(game_over, (width // 2 - 180, height // 2 - 40))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Реверсивное управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and buttons['w']:
        dx, dy = 0, 1     # Реверс: вверх -> вниз
        buttons = {'w': True, 's': False, 'a': True, 'd': True}
    if key[pygame.K_s] and buttons['s']:
        dx, dy = 0, -1    # Реверс: вниз -> вверх
        buttons = {'w': False, 's': True, 'a': True, 'd': True}
    if key[pygame.K_a] and buttons['a']:
        dx, dy = 1, 0     # Реверс: влево -> вправо
        buttons = {'w': True, 's': True, 'a': True, 'd': False}
    if key[pygame.K_d] and buttons['d']:
        dx, dy = -1, 0    # Реверс: вправо -> влево
        buttons = {'w': True, 's': True, 'a': False, 'd': True}

    # Сброс игры
    if key[pygame.K_SPACE]:
        sc.blit(bg, (0, 0))
        x, y = randrange(100, width - 100, size), randrange(100, height - 100, size)
        snake = [(x, y)]
        Shroom = randrange(20, width - 20, size), randrange(40, height - 20, size)
        score = 0
        length = 1
        dx, dy = 0, 0
        fps = 5
