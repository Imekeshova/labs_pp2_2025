import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 1100, 700  # Увеличили ширину для новых кнопок
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #рисуем дисплей
pygame.display.set_caption("lab 9 Paint")

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
current_tool = "pen"  # 'pen', 'rect', 'circle', 'eraser', 'square', 'rtriangle', 'etriangle', 'rhombus'
screen.fill(BLACK)

# Кнопки инструментов
buttons = [
    {"rect": pygame.Rect(10, 10, 80, 40), "text": "Pen", "tool": "pen"},
    {"rect": pygame.Rect(100, 10, 80, 40), "text": "Rect", "tool": "rect"},
    {"rect": pygame.Rect(190, 10, 80, 40), "text": "Circle", "tool": "circle"},
    {"rect": pygame.Rect(280, 10, 80, 40), "text": "Eraser", "tool": "eraser"},
    # Новые кнопки (размещаем их справа От цветов)
    {"rect": pygame.Rect(710, 10, 80, 40), "text": "Square", "tool": "square"},
    {"rect": pygame.Rect(800, 10, 80, 40), "text": "E Tri-ale", "tool": "rtriangle"},
    {"rect": pygame.Rect(890, 10, 80, 40), "text":  "R Tri-ale", "tool": "etriangle"},
    {"rect": pygame.Rect(980, 10, 80, 40), "text": "Rhomb", "tool": "rhombus"}
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
        if event.type == pygame.QUIT: # Организуем выход из программы с помошью проверки события
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
                        elif current_tool != "eraser" and current_color == BLACK:
                            current_color = WHITE

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
            if current_tool == "rect": #прямоугольник
                width = event.pos[0] - last_pos[0]
                height = event.pos[1] - last_pos[1]
                pygame.draw.rect(screen, current_color, (last_pos[0], last_pos[1], width, height), 2)
            elif current_tool == "circle": #круг
                radius = ((event.pos[0] - last_pos[0]) ** 2 + (event.pos[1] - last_pos[1]) ** 2) ** 0.5
                pygame.draw.circle(screen, current_color, last_pos, int(radius), 2)
            elif current_tool == "square":  # Квадрат
                size = max(abs(event.pos[0] - last_pos[0]), abs(event.pos[1] - last_pos[1]))
                left = min(last_pos[0], event.pos[0])
                top = min(last_pos[1], event.pos[1])
                pygame.draw.rect(screen, current_color, (left, top, size, size), 2)
            elif current_tool == "rtriangle":  # Прямоугольный треугольник
                points = [
                    last_pos,
                    (event.pos[0], last_pos[1]),
                    (last_pos[0], event.pos[1])
                ]
                pygame.draw.polygon(screen, current_color, points, 2)
            elif current_tool == "etriangle":  # Равносторонний треугольник
                width = event.pos[0] - last_pos[0]
                height = math.sqrt(3) * abs(width) / 2
                if width < 0:
                    height = -height
                points = [
                    last_pos,
                    (last_pos[0] + width, last_pos[1]),
                    (last_pos[0] + width/2, last_pos[1] - height)
                ]
                pygame.draw.polygon(screen, current_color, points, 2)
            elif current_tool == "rhombus":  # Ромб
                center_x = (last_pos[0] + event.pos[0]) / 2
                center_y = (last_pos[1] + event.pos[1]) / 2
                width = abs(event.pos[0] - last_pos[0]) / 2
                height = abs(event.pos[1] - last_pos[1]) / 2
                points = [
                    (center_x, center_y - height),
                    (center_x + width, center_y),
                    (center_x, center_y + height),
                    (center_x - width, center_y)
                ]
                pygame.draw.polygon(screen, current_color, points, 2)

    # Отрисовка интерфейса
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, WIDTH, 60))  # Панель инструментов в сером цвете и ее параметры

    # Отрисовка кнопок инструментов
    for button in buttons:
        if current_tool == button["tool"]: # Если кнопка нажата меняем цвет на более светлый оттенок
            button_color = (100, 100, 100)
        else:
            button_color = (70, 70, 70)
        
        pygame.draw.rect(screen, button_color, button["rect"])  
        
        button_font = pygame.font.SysFont(None, 24)
        button_text = button_font.render(button["text"], True, WHITE)
        
        text_x = button["rect"].x + 10
        text_y = button["rect"].y + 10
        screen.blit(button_text, (text_x, text_y))

    # Отрисовка кнопок цветов
    for btn in color_buttons:
        pygame.draw.rect(screen, btn["color"], btn["rect"])
        if current_color == btn["color"] and current_tool != "eraser":
            pygame.draw.rect(screen, WHITE, btn["rect"], 2)  # Обводка выбранного цвета белым

    pygame.display.flip()
    clock.tick(60)