import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [ 
    (255, 255, 255),  # Белый
    (128, 0, 128),    # Фиолетовый
    (0, 0, 255),      # Синий
    (0, 255, 255),    # Голубой
    (0, 128, 0),      # Зелёный
    (255, 255, 0),    # Жёлтый
    (255, 165, 0),    # Оранжевый
    (255, 0, 0)       # Красный
]

# Настройки рисования
drawing = False
last_pos = None
current_color = WHITE
current_tool = "pen"  # 'pen', 'rect', 'circle', 'eraser'
screen.fill(BLACK)

# Кнопки инструментов
buttons = [
    {"rect": pygame.Rect(10, 10, 80, 40), "text": "Pen", "tool": "pen"},
    {"rect": pygame.Rect(100, 10, 80, 40), "text": "Rect", "tool": "rect"},
    {"rect": pygame.Rect(190, 10, 80, 40), "text": "Circle", "tool": "circle"},
    {"rect": pygame.Rect(280, 10, 80, 40), "text": "Eraser", "tool": "eraser"}
]

# Кнопки цветов
color_buttons = []
for i, color in enumerate(COLORS):
    color_buttons.append({
        "rect": pygame.Rect(380 + i * 40, 10, 35, 35),
        "color": color
    })

# Основной цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Обработка нажатия мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
                last_pos = event.pos

                # Проверка нажатия на кнопки инструментов
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        current_tool = button["tool"]
                        if current_tool == "eraser":
                            current_color = BLACK

                # Проверка нажатия на кнопки цветов
                for btn in color_buttons:
                    if btn["rect"].collidepoint(event.pos):
                        current_color = btn["color"]
                        current_tool = "pen"  # Переключаемся на карандаш при выборе цвета

        # Обработка движения мыши (рисование)
        if event.type == pygame.MOUSEMOTION and drawing:
            if current_tool == "pen":
                pygame.draw.line(screen, current_color, last_pos, event.pos, 3)
                last_pos = event.pos
            elif current_tool == "eraser":
                pygame.draw.line(screen, BLACK, last_pos, event.pos, 10)
                last_pos = event.pos

        # Обработка отпускания кнопки мыши (завершение фигуры)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            if current_tool == "rect":
                width = event.pos[0] - last_pos[0]
                height = event.pos[1] - last_pos[1]
                pygame.draw.rect(screen, current_color, (last_pos[0], last_pos[1], width, height), 2)
            elif current_tool == "circle":
                radius = ((event.pos[0] - last_pos[0]) ** 2 + (event.pos[1] - last_pos[1]) ** 2) ** 0.5
                pygame.draw.circle(screen, current_color, last_pos, int(radius), 2)

    # Отрисовка интерфейса
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, WIDTH, 60))  # Панель инструментов

    # Отрисовка кнопок инструментов (развёрнутая версия)
    for button in buttons:
        # Заменяем тернарный оператор на полную версию if-else
        if current_tool == button["tool"]:
            # Если это активная кнопка - более светлый серый
            button_color = (100, 100, 100)
        else:
            # Если неактивная - более тёмный серый
            button_color = (70, 70, 70)
        
        # Рисуем прямоугольник кнопки
        pygame.draw.rect(screen, button_color, button["rect"])
        
        # Создаём шрифт
        button_font = pygame.font.SysFont(None, 24)
        
        # Создаём текст
        button_text = button_font.render(button["text"], True, WHITE)
        
        # Размещаем текст на кнопке (с отступами)
        text_x = button["rect"].x + 10
        text_y = button["rect"].y + 10
        screen.blit(button_text, (text_x, text_y))

    # Отрисовка кнопок цветов
    for btn in color_buttons:
        pygame.draw.rect(screen, btn["color"], btn["rect"])

    pygame.display.flip()
    clock.tick(60)