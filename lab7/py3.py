import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
radius = 25
x, y = 250, 250
speed = 20  

running = True
while running:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - radius > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius < 500:
        x += speed
    if keys[pygame.K_UP] and y - radius > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius < 500:
        y += speed

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.update()

pygame.quit()
