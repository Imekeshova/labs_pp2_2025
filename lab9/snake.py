import pygame  
import random 
import time    
import sys     

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 600  # Размер игрового поля
GRID_SIZE = 30            # Размер одного сегмента змейки/еды
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создаем окно
pygame.display.set_caption("Змейка с уровнями и разной едой")  # Заголовок окна
clock = pygame.time.Clock()  # Для контроля FPS

# Цвета
BLACK = (0, 0, 0)         
SNAKE_COLOR = (244, 193, 193)  # Розовый цвет змейки
RED = (255, 0, 0)          # Красная еда (вес 1)
YELLOW = (255, 255, 0)     # Желтая еда (вес 2)
GREEN = (0, 255, 0)        # Зеленая еда (вес 3)
WHITE = (255, 255, 255)    # Белый цвет текста

# Шрифты для текста
font_large = pygame.font.SysFont('Verdana', 40) 
font_small = pygame.font.SysFont('Verdana', 20)  

# Границы игрового поля
BORDER_LEFT = 0
BORDER_TOP = 0
BORDER_RIGHT = WIDTH - GRID_SIZE
BORDER_BOTTOM = HEIGHT - GRID_SIZE

# Класс для еды
class Food:
    def __init__(self, pos, weight):
        self.pos = pos            # Позиция еды [x, y]
        self.weight = weight      # Вес/ценность еды (1, 2 или 3)
        self.spawn_time = time.time()  # Время создания еды
        self.lifetime = random.uniform(5, 10)  # Время жизни еды (5-10 сек)
        
    def is_expired(self):
        # Проверяем, не истекло ли время жизни еды
        return time.time() - self.spawn_time > self.lifetime
        
    def get_color(self):
        # Возвращаем цвет в зависимости от веса еды
        if self.weight == 1:
            return RED
        elif self.weight == 2:
            return YELLOW
        else:
            return GREEN

# Основной класс игры
class Game:
    def __init__(self):
        self.reset()  # Инициализируем игру
        
    def reset(self):
        # Сбрасываем состояние игры
        self.snake = [[300, 300]]  # Начальная позиция змейки
        self.direction = [GRID_SIZE, 0]  # Начальное направление (вправо)
        self.food = self.create_food()  # Создаем первую еду
        self.score = 0           # Начальный счет
        self.level = 1           # Начальный уровень
        self.speed = 8           # Начальная скорость
        self.game_over = False    # Флаг окончания игры
        self.next_level_score = 15  # Очков до следующего уровня
    
    def create_food(self):
        # Создаем новую еду на случайной позиции
        while True:
            # Генерируем случайную позицию, выровненную по сетке
            food_pos = [
                random.randrange(BORDER_LEFT + GRID_SIZE, BORDER_RIGHT, GRID_SIZE),
                random.randrange(BORDER_TOP + GRID_SIZE, BORDER_BOTTOM, GRID_SIZE)
            ]
            # Проверяем, чтобы еда не появилась на змейке
            if food_pos not in self.snake:
                # Выбираем вес еды с разной вероятностью
                weight = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
                return Food(food_pos, weight)
    
    def check_collision(self):
        # Создаем прямоугольник для головы змейки
        head_rect = pygame.Rect(self.snake[0][0], self.snake[0][1], GRID_SIZE, GRID_SIZE)
        
        # Проверка выхода за границы игрового поля
        if (head_rect.left < BORDER_LEFT or head_rect.right > BORDER_RIGHT + GRID_SIZE or
            head_rect.top < BORDER_TOP or head_rect.bottom > BORDER_BOTTOM + GRID_SIZE):
            return True
        
        # Проверка столкновения головы с телом змейки
        for segment in self.snake[1:]:
            segment_rect = pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE)
            if head_rect.colliderect(segment_rect):
                return True
                
        return False
    
    def update(self):
        # Обновляем состояние игры
        if self.game_over:
            return
            
        # Движение змейки - добавляем новую голову
        new_head = [self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1]]
        self.snake.insert(0, new_head)
        
        # Проверка, съела ли змейка еду
        if self.snake[0] == self.food.pos:
            self.score += self.food.weight  # Увеличиваем счет
            self.food = self.create_food()  # Создаем новую еду
            
            # Проверка перехода на новый уровень
            if self.score >= self.next_level_score:
                self.level += 1      # Увеличиваем уровень
                self.speed += 2      # Увеличиваем скорость
                self.next_level_score += 15  # Увеличиваем порог для следующего уровня
        else:
            # Если еда не съедена - удаляем хвост
            self.snake.pop()
        
        # Проверка, не исчезла ли еда
        if self.food.is_expired():
            self.food = self.create_food()
        
        # Проверка столкновений
        if self.check_collision():
            self.game_over = True  # Игра окончена
            self.game_over_time = time.time()  # Запоминаем время окончания
    
    def draw(self):
        # Отрисовка игрового состояния
        screen.fill(BLACK)  # Заливаем фон черным
        
        # Рисуем змейку
        for segment in self.snake:
            pygame.draw.rect(screen, SNAKE_COLOR, 
                           (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
        
        # Рисуем еду
        pygame.draw.rect(screen, self.food.get_color(), 
                       (self.food.pos[0], self.food.pos[1], GRID_SIZE, GRID_SIZE))
        
        # Отображаем счет и уровень
        score_text = font_small.render(f"Score: {self.score}", True, WHITE)
        level_text = font_small.render(f"Level: {self.level}", True, WHITE)
        
        screen.blit(score_text, (10, 10))  # Позиция счета
        screen.blit(level_text, (10, 40))  # Позиция уровня
        
        # Если игра окончена
        if self.game_over:
            text = font_large.render("GAME OVER", True, WHITE)
            # Центрируем текст
            screen.blit(text, (WIDTH//2 - text.get_width()//2, 
                             HEIGHT//2 - text.get_height()//2))
            pygame.display.update()  # Обновляем экран
            
            # Ждем 1 секунду перед выходом
            if time.time() - self.game_over_time > 1:
                pygame.quit()
                sys.exit()

game = Game()

# Основной игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие окна
            pygame.quit()
            sys.exit()
        # Обработка нажатий клавиш (только если игра не окончена)
        if not game.game_over and event.type == pygame.KEYDOWN:
            # Вверх (проверяем, чтобы не двигаться вниз)
            if event.key == pygame.K_UP and game.direction != [0, GRID_SIZE]:
                game.direction = [0, -GRID_SIZE]
            # Вниз (проверяем, чтобы не двигаться вверх)
            elif event.key == pygame.K_DOWN and game.direction != [0, -GRID_SIZE]:
                game.direction = [0, GRID_SIZE]
            # Влево (проверяем, чтобы не двигаться вправо)
            elif event.key == pygame.K_LEFT and game.direction != [GRID_SIZE, 0]:
                game.direction = [-GRID_SIZE, 0]
            # Вправо (проверяем, чтобы не двигаться влево)
            elif event.key == pygame.K_RIGHT and game.direction != [-GRID_SIZE, 0]:
                game.direction = [GRID_SIZE, 0]
    
    # Обновляем и рисуем игру
    game.update()
    game.draw()
    pygame.display.update() 
    clock.tick(game.speed) 