import pygame


if __name__ == '__main__':
    pygame.init()
    size = (700, 500)
    screen_height = size[0]
    screen_width = size[1]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Heli")
    clock= pygame.time.Clock()


    heli_right = pygame.image.load("heli_right.png")
    heli_right = pygame.transform.scale(heli_right,(64,64))

    heli_left = pygame.image.load("heli_left.png")
    heli_left = pygame.transform.scale(heli_left,(64,64))

    background = pygame.image.load("plx-5.png")
    background = pygame.transform.scale(background,(700,500))

    x= screen_height//2 - screen_height//20
    y = screen_width//2 - screen_width//20

    dx = 0
    dy = 0
    flying_up = False
    heading_right = True

    game_over = False
    while not game_over:
        x = x+dx
        y = y+dy
        if flying_up:
            dy = dy-1
        else:
            dy = dy+1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # if event.type = pygame.K

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -10
                    heading_right = False
                if event.key == pygame.K_RIGHT:
                    dx = 10
                    heading_right = True
                if event.key == pygame.K_UP:
                    flying_up = True
                if event.key == pygame.K_DOWN:
                    dy = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if dx<0:
                        dx = 0
                if event.key == pygame.K_RIGHT:
                    if dx>0:
                        dx = 0
                if event.key == pygame.K_UP:
                    flying_up = False
                if event.key == pygame.K_DOWN:
                    if dy>0:
                        dy = 0

        screen.fill((255,255,255))
        screen.blit(background,(0,0))
        if heading_right:
            screen.blit(heli_right,(x,y))
        else:
            screen.blit(heli_left, (x, y))
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
