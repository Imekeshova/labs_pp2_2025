import pygame

pygame.init()


WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

PINK = (255, 192, 203)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 50)


playlist = ["music1.mp3", "music2.mp3", "music3.mp3"]
current_track = 0  


def play_track():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()


play_track()

def draw_text(text, x, y):
    render = font.render(text, True, BLACK)
    screen.blit(render, (x, y))


running = True
paused = False

while running:
    screen.fill(PINK)  
   
    track_text = f"Track: {playlist[current_track]}"
    draw_text(track_text, 20, 20)

    play_pause_hint = "SPACE - Play/Pause"
    draw_text(play_pause_hint, 80, 130)

    next_prev_hint = "N - Next | P - Previous"
    draw_text(next_prev_hint, 80, 200)


    pygame.display.flip()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False

            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                play_track()

            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(playlist)
                play_track()

pygame.quit()
