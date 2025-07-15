import pygame

def draw_grid():
    block_size = 72
    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range(0, WINDOW_HEIGHT, block_size):
            rect = pygame.Rect(x,y,block_size,block_size)
            pygame.draw.rect(screen,"blue",rect,1)

pygame.init()
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    draw_grid()

    

    pygame.display.update()

    clock.tick(60)

pygame.quit()   