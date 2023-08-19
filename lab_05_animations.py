import pygame as pg
import math
import module5 as m5
pg.init()
WIDTH = 400
HEIGHT = 400
FPS = 60

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
speed = -5
x1 = 200
y1 = 250
a = b = 200
bg = pg.image.load("/Users/admin/Desktop/питон/labs_2sem/1675435428_bogatyr-club-p-fon-v-kletku-fon-vkontakte-14.png")
compas = pg.image.load("/Users/admin/Desktop/питон/labs_2sem/Unknown.png")
compas = pg.transform.scale(compas, (100, 100))
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Lab 5")
last_speed = speed
i = 0
x0 = y0 = 200
clock = pg.time.Clock()
running = True
left = True
right = False
temp_y = 100
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q and (left != False or right != False):
                last_left= left
                last_right = right
                left = False
                right = False
                last_speed = speed
                speed = 0
            elif event.key == pg.K_q and (left == False and right == False):
                left = last_left
                right = last_right
                speed = last_speed
            elif event.key == pg.K_SPACE:
                if left == True:
                    left = False
                    right = True
                else:
                    left = True
                    right = False
                speed = last_speed
                speed = -speed
    if right ==True:
        i, a, b = m5.move_right(i, a, x0, y0)
    elif left == True:
        i, a, b = m5.move_left(i, a, x0, y0)
    if temp_y <= 100 or temp_y >=300:
        speed = -speed
    temp_y+=speed
    win.fill(WHITE)
    win.blit(bg, (0, 0))

    # temperature
    pg.draw.line(win, BLUE, (50, 100), (50, 300), 6)
    pg.draw.line(win, RED, (50, 100), (50, temp_y), 6)
    pg.draw.circle(win, BLACK, (50, temp_y), 10)
    # compas
    pg.draw.circle(win, WHITE, (200, 200), 100)
    pg.draw.circle(win, RED, (200, 200), 100, 1)
    win.blit(compas, (150, 150))
    pg.draw.line(win, RED, (int(a), int(b)),(200, 200), 6)
    pg.draw.line(win, BLUE, (400 - int(a), 400 - int(b)), (200, 200), 6)
    pg.display.flip()
    clock.tick(FPS)
