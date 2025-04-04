# Импортируем необходимые библиотеки
import pygame  # Основная библиотека для создания игры
import sys     # Для работы с системными функциями (например, выход из игры)
import time    # Для работы со временем (например, задержка перед выходом)
import random  # Для генерации случайных чисел (позиции врагов и монет)
from pygame.locals import *  # Импортируем константы Pygame

# Инициализация всех модулей Pygame
pygame.init()

# Настройка FPS для плавности игры
FPS = 60  # Количество кадров в секунду
FramePerSec = pygame.time.Clock()  # Создаем объект для контроля FPS

# Создаем цвета в формате RGB
BLUE  = (0, 0, 255)     # Синий
RED   = (255, 0, 0)     # Красный
GREEN = (0, 255, 0)     # Зеленый
BLACK = (0, 0, 0)       # Черный
WHITE = (255, 255, 255) # Белый
GOLD  = (255, 215, 0)   # Золотой

# Основные переменные игры
SCREEN_WIDTH = 400    # Ширина игрового окна
SCREEN_HEIGHT = 600   # Высота игрового окна
SPEED = 5             # Начальная скорость врагов
SCORE = 0             # Счетчик очков (за проезд машин)
COINS = 0             # Счетчик собранных монет
COIN_SPEED_BOOST = 5  # Ускорение врагов каждые 5 монет

# Настройка шрифтов для текста в игре
font = pygame.font.SysFont("Verdana", 60)       # Большой шрифт для "Game Over"
font_small = pygame.font.SysFont("Verdana", 20) # Малый шрифт для счетчиков
game_over = font.render("Game Over", True, BLACK)  # Текст "Game Over"

# Загружаем изображения с обработкой ошибок
try:
    background = pygame.image.load("AnimatedStreet.png")  # Фон игры
    player_img = pygame.image.load("Player.png")          # Изображение игрока
    enemy_img = pygame.image.load("Enemy.png")            # Изображение врага
    coin_img = pygame.image.load("coinn.png")             # Изображение монеты
except:
    print("Ошибка загрузки изображений!")
    pygame.quit()  # Закрываем Pygame при ошибке
    sys.exit()     # Выходим из программы

# Создаем игровое окно
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Устанавливаем размер окна
DISPLAYSURF.fill(WHITE)  # Заливаем белым цветом (временно)
pygame.display.set_caption("Racer with Coins")  # Устанавливаем заголовок окна

# Класс для монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Инициализируем родительский класс
        try:
            original_image = pygame.image.load("coinn.png")
            self.image = pygame.transform.scale(original_image, (30, 30))  # Масштабируем изображение
            self.rect = self.image.get_rect()  # Получаем прямоугольник для коллизий
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  # Случайная позиция по X
            self.weight = random.choice([1, 2, 3])  # Вес монеты (1, 2 или 3 очка)
        except:
            print("Не удалось загрузить изображение монеты!")
            pygame.quit()
            sys.exit()

    def move(self):
        self.rect.move_ip(0, 3)  # Двигаем монету вниз
        if self.rect.top > SCREEN_HEIGHT:  # Если монета ушла за экран
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  # Возвращаем в начало

# Класс для врагов (машин)
class Enemy(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.image = enemy_img  # Устанавливаем изображение врага
        self.rect = self.image.get_rect()  # Получаем прямоугольник для коллизий
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Случайная позиция
    
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Двигаем врага вниз с текущей скоростью
        if self.rect.bottom > SCREEN_HEIGHT:  # Если враг ушел за экран
            SCORE += 1  # Увеличиваем счет
            self.rect.top = 0  # Возвращаем в начало
            self.rect.center = (random.randint(30, 370), 0)  # Новая случайная позиция
    
# Класс для игрока        
class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = player_img  # Устанавливаем изображение игрока
        self.rect = self.image.get_rect()  # Получаем прямоугольник для коллизий
        self.rect.center = (160, 520)  # Начальная позиция игрока
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
        if self.rect.left > 0 and pressed_keys[K_LEFT]:  # Движение влево
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:  # Движение вправо
            self.rect.move_ip(5, 0)

# Создаем экземпляры спрайтов
P1 = Player()  # Игрок
E1 = Enemy()   # Враг
C1 = Coin()    # Монета

# Создаем группы спрайтов
enemies = pygame.sprite.Group()  # Группа для врагов
enemies.add(E1)
coins = pygame.sprite.Group()    # Группа для монет
coins.add(C1)

all_sprites = pygame.sprite.Group()  # Группа для всех спрайтов
all_sprites.add(P1)
all_sprites.add(E1) 
all_sprites.add(C1)

# Создаем пользовательское событие для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Таймер - каждую секунду

# Загружаем звуки с обработкой ошибок
try:
    crash_sound = pygame.mixer.Sound('crash.wav')  # Звук столкновения
except:
    crash_sound = None  
    

# Основной игровой цикл
while True:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == INC_SPEED:  # Событие увеличения скорости
            SPEED += 0.5
        if event.type == QUIT:       # Событие закрытия окна
            pygame.quit()
            sys.exit()
    
    # Отрисовка игровых элементов
    DISPLAYSURF.blit(background, (0, 0))  # Рисуем фон
    # Создаем тексты счетчиков
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    # Размещаем счетчики на экране
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH-120, 10))
    
    # Обновляем и рисуем все спрайты
    for entity in all_sprites:
        entity.move()  # Двигаем спрайт
        DISPLAYSURF.blit(entity.image, entity.rect)  # Рисуем спрайт
    
    # Проверка сбора монет
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)  # Проверяем столкновения
    for coin in collected_coins:  # Обрабатываем каждую собранную монету
        COINS += coin.weight  # Увеличиваем счет монет
        # Создаем новую монету
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
        
        # Ускоряем врагов каждые COIN_SPEED_BOOST монет
        if COINS % COIN_SPEED_BOOST == 0:
            SPEED += 1
    
    # Проверка столкновения с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        if crash_sound:
            crash_sound.play()  # Проигрываем звук столкновения
        DISPLAYSURF.fill(RED)  # Заливаем экран красным
        DISPLAYSURF.blit(game_over, (30, 250))  
        pygame.display.update()  # Обновляем экран
        time.sleep(2)  # Ждем 2 секунды
        pygame.quit()  
        sys.exit()     

    pygame.display.update()  # Обновляем экран
    FramePerSec.tick(FPS)   