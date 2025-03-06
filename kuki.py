import pygame
import math
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
def rysunek():
    pygame.draw.circle(screen, (190, 190, 190), (400, 400), 200)
    pygame.draw.polygon(screen, (195, 195, 195), ((200, 170), (230, 300), (330, 220)))
    pygame.draw.polygon(screen, (195, 195, 195), ((470, 220), (570, 300), (600, 170)))
    pygame.draw.polygon(screen, (255, 170, 200), ((350, 400), (450, 400), (400, 440)))
    pygame.draw.circle(screen, (255, 255, 255), (320, 350), 30)
    pygame.draw.circle(screen, (255, 255, 255), (480, 350), 30)
    pygame.draw.line(screen, (255, 170, 200), (400, 440), (370, 470), 5)
    pygame.draw.line(screen, (255, 170, 200), (400, 440), (430, 470), 5)
def oczy():
    kordy = (pygame.mouse.get_pos())
    dx = kordy[0] - 400
    dy = kordy[1] - 350
    if (dx != 0):
        alfa = math.degrees(math.atan2(dy, dx))
        print(alfa)
    else:
        alfa = 0
        print(alfa)
    x = math.cos(math.radians(alfa)) * 10
    y = math.sin(math.radians(alfa)) * 10
    pygame.draw.circle(screen, (0, 0, 0), (320 + x, 350 + y), 10)
    pygame.draw.circle(screen, (0, 0, 0), (480 + x, 350 + y), 10)


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    rysunek()
    oczy()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
