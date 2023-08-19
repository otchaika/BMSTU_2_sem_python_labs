import pygame
import math

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Компас")

circle_radius = 50
circle_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

compass_image = pygame.image.load('/Users/admin/Desktop/питон/labs_2sem/penguin1.png')
compass_image = pygame.transform.scale(compass_image, (circle_radius * 4, circle_radius * 4))
compass_rect = compass_image.get_rect(center=circle_pos)

angle = 0

def get_angle():
    dx = circle_pos[0] - mouse_pos[0]
    dy = circle_pos[1] - mouse_pos[1]
    return math.degrees(math.atan2(dy, dx)) + 180

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            continue
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            angle = get_angle()

    screen.fill((255, 255, 255))

    rotated_image = pygame.transform.rotate(compass_image, angle)
    compass_rect = rotated_image.get_rect(center=compass_rect.center)

    screen.blit(rotated_image, compass_rect)

    pygame.draw.circle(screen, (0, 0, 0), circle_pos, circle_radius)

    pygame.display.flip()

pygame.quit()
