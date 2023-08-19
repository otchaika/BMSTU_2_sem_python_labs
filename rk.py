import pygame
import math as m
import rk_mod as r
pygame.init()
FPS = 60
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("RKь")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
x = 1
y = 100
angle = 0
clock = pygame.time.Clock()
x2, y2  =210, 110
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    win.fill((0, 0, 0))
    pygame.draw.ellipse(win, WHITE, (10*m.sin(x)+110, -10*x+110, 100, 50))
    pygame.draw.line(win, WHITE, (10*m.sin(x)+110, -10*x+170), (10*m.sin(x)+210, -10*x+170), 3)
    pygame.draw.line(win, WHITE, (10 * m.sin(x) + 160, -10 * x + 160), (10 * m.sin(x) + 160, -10 * x + 170), 3)
    pygame.draw.line(win, WHITE, (10 * m.sin(x) + 170, -10 * x + 160), (10 * m.sin(x) + 170, -10 * x + 170), 3)
    pygame.draw.line(win, WHITE, (10 * m.sin(x) + 110, -10 * x + 170), (10 * m.sin(x) + 110, -10 * x + 160), 3)

    pygame.draw.rect(win, RED, (10*m.sin(x)+130, -10*x+130, 20, 20))
    pygame.draw.line(win, WHITE, (10 * m.sin(x) + 160, -10 * x + 110), (10 * m.sin(x) + 160, -10 * x + 100), 3)
    # лопасти

    x1 = 10*m.sin(x)+160
    y1 = -10*x+100

    x2, y2 = r.rotate_lop(x2, y2, x1, y1, angle +90)
    x3, y3 = r.rotate_lop(x2, y2, x1, y1, angle)
    x4, y4 = r.rotate_lop(x2, y2, x1, y1, angle + 180)
    x5, y5 = r.rotate_lop(x2, y2, x1, y1, angle + 270)
    angle +=1
    if angle == 360:
        angle = 0
    pygame.draw.line(win, WHITE, (x1, y1), (x2, y2), 3)
    pygame.draw.line(win, WHITE, (x1, y1), (x3, y3), 3)
    pygame.draw.line(win, WHITE, (x1, y1), (x4, y4), 3)
    pygame.draw.line(win, WHITE, (x1, y1), (x5, y5), 3)
    if -10*x+100 < 0:
        x = -20
    x+=0.1
    pygame.display.flip()
    clock.tick(FPS)