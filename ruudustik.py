import pygame


pygame.init()

red = [255, 0, 0]
lGreen = [153, 255, 153]


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Varuskin - IS22")
screen.fill(lGreen)


def draw_squares(size, rows, columns, color):
    for row in range(rows):
        for column in range(columns):
            square = pygame.Rect(column * size, row * size, size, size)
            pygame.draw.rect(screen, color, square, 1)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_squares(20, 24, 32, (red))

    pygame.display.update()