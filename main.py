import pygame


if __name__ == '__main__':
    pygame.init()
    size = (700, 500)
    screen_height = size[0]
    screen_width = size[1]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Heli")
    clock= pygame.time.Clock()


    heli = pygame.image.load("heli_right.png")
    heli = pygame.transform.scale(heli,(64,64))

    background = pygame.image.load("plx-5.png")
    background = pygame.transform.scale(background,(700,500))

    x= screen_height//2 - screen_height//20
    y = screen_width//2 - screen_width//20

    dx = 0
    dy = 0

    game_over = False
    while not game_over:
        x = x+dx
        y = y+dy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # if event.type = pygame.K

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if dx >0 :
                        dx = 0
                    else:
                        dx = -10
                if event.key == pygame.K_RIGHT:
                    if dx < 0:
                        dx = 0
                    else:
                        dx = 10
                if event.key == pygame.K_UP:
                    if dy>0:
                        dy = 0
                    else:
                        dy = -10
                if event.key == pygame.K_DOWN:
                    if dy<0:
                        dy = 0
                    else:
                        dy = 10

        screen.fill((255,255,255))
        screen.blit(background,(0,0))
        screen.blit(heli,(x,y))
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
