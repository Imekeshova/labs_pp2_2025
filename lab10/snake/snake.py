import pygame  
import random 
import time    
import psycopg2
import sys

from user_login import get_or_create_user
from save_progress import save_progress

# Ввод имени и загрузка прогресса
username = input("Введите имя пользователя: ")
user_id, (start_level, start_score) = get_or_create_user(username)

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка с уровнями и разной едой")
clock = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
SNAKE_COLOR = (244, 193, 193)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Шрифты
font_large = pygame.font.SysFont('Verdana', 40) 
font_small = pygame.font.SysFont('Verdana', 20)  

# Границы
BORDER_LEFT = 0
BORDER_TOP = 0
BORDER_RIGHT = WIDTH - GRID_SIZE
BORDER_BOTTOM = HEIGHT - GRID_SIZE

class Food:
    def __init__(self, pos, weight):
        self.pos = pos
        self.weight = weight
        self.spawn_time = time.time()
        self.lifetime = random.uniform(5, 10)
        
    def is_expired(self):
        return time.time() - self.spawn_time > self.lifetime
        
    def get_color(self):
        if self.weight == 1:
            return RED
        elif self.weight == 2:
            return YELLOW
        else:
            return GREEN

class Game:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.snake = [[300, 300]]
        self.direction = [GRID_SIZE, 0]
        self.food = self.create_food()
        self.score = start_score
        self.level = start_level
        self.speed = 2 + (self.level - 1) * 2
        self.next_level_score = 15 * self.level
        self.game_over = False
        self.paused = False
    
    def create_food(self):
        while True:
            food_pos = [
                random.randrange(BORDER_LEFT + GRID_SIZE, BORDER_RIGHT, GRID_SIZE),
                random.randrange(BORDER_TOP + GRID_SIZE, BORDER_BOTTOM, GRID_SIZE)
            ]
            if food_pos not in self.snake:
                weight = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
                return Food(food_pos, weight)
    
    def check_collision(self):
        head_rect = pygame.Rect(self.snake[0][0], self.snake[0][1], GRID_SIZE, GRID_SIZE)
        if (head_rect.left < BORDER_LEFT or head_rect.right > BORDER_RIGHT + GRID_SIZE or
            head_rect.top < BORDER_TOP or head_rect.bottom > BORDER_BOTTOM + GRID_SIZE):
            return True
        for segment in self.snake[1:]:
            segment_rect = pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE)
            if head_rect.colliderect(segment_rect):
                return True
        return False
    
    def update(self):
        if self.game_over or self.paused:
            return
        new_head = [self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1]]
        self.snake.insert(0, new_head)
        
        if self.snake[0] == self.food.pos:
            self.score += self.food.weight
            self.food = self.create_food()
            if self.score >= self.next_level_score:
                self.level += 1
                self.speed += 1
                self.next_level_score += 15
        else:
            self.snake.pop()
        
        if self.food.is_expired():
            self.food = self.create_food()
        
        if self.check_collision():
            self.game_over = True
            self.game_over_time = time.time()
    
    def draw(self):
        screen.fill(BLACK)
        for segment in self.snake:
            pygame.draw.rect(screen, SNAKE_COLOR, 
                             (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.food.get_color(), 
                         (self.food.pos[0], self.food.pos[1], GRID_SIZE, GRID_SIZE))
        score_text = font_small.render(f"Score: {self.score}", True, WHITE)
        level_text = font_small.render(f"Level: {self.level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))

        if self.paused:
            pause_text = font_large.render("PAUSED", True, WHITE)
            screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2,
                                     HEIGHT // 2 - pause_text.get_height() // 2))

        if self.game_over:
            text = font_large.render("GAME OVER", True, WHITE)
            screen.blit(text, (WIDTH//2 - text.get_width()//2, 
                               HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            if time.time() - self.game_over_time > 1:
                save_progress(user_id, self.level, self.score)
                print("Прогресс сохранен при завершении игры.")
                pygame.quit()
                sys.exit()

game = Game()

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress(user_id, game.level, game.score)
            print("Прогресс сохранен при выходе.")
            pygame.quit()
            sys.exit()
        if not game.game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.direction != [0, GRID_SIZE]:
                game.direction = [0, -GRID_SIZE]
            elif event.key == pygame.K_DOWN and game.direction != [0, -GRID_SIZE]:
                game.direction = [0, GRID_SIZE]
            elif event.key == pygame.K_LEFT and game.direction != [GRID_SIZE, 0]:
                game.direction = [-GRID_SIZE, 0]
            elif event.key == pygame.K_RIGHT and game.direction != [-GRID_SIZE, 0]:
                game.direction = [GRID_SIZE, 0]
            elif event.key == pygame.K_p:
                game.paused = not game.paused
                if game.paused:
                    save_progress(user_id, game.level, game.score)
                    print("Игра на паузе. Прогресс сохранен.")
                else:
                    print("Игра продолжена.")

    game.update()
    game.draw()
    pygame.display.update()
    clock.tick(game.speed)