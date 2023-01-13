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
    heli_right = pygame.transform.scale(heli_right,(screen_width//10,screen_height//10))

    heli_left = pygame.image.load("heli_left.png")
    heli_left = pygame.transform.scale(heli_left,(screen_width//10,screen_height//10))

    background = pygame.image.load("plx-5.png")
    background = pygame.transform.scale(background,(700,500))

    x= screen_height//2 - screen_height//20
    y = screen_width//2 - screen_width//20

    dx = 0
    dy = 0
    flying_up = False
    heading_right = True

    platforms = [pygame.Rect(0, 0, 40, 500),
                 pygame.Rect(0, 450, 500, 40),
                 pygame.Rect(100, 100, 300, 40),
                 pygame.Rect(500, 200, 100, 40),]
    game_over = False
    while not game_over:
        if flying_up:
            dy = dy-1
            if dy<-10:
                dy=-10
        else:
            dy = dy+0.5
            if dy>10:
                dy=10

        x = x+dx
        heli_rect = pygame.Rect(x,y,screen_width//10,screen_height//12)
        for platform in platforms:
            if heli_rect.colliderect(platform):
                x = x-dx


        y = y+dy
        heli_rect = pygame.Rect(x,y,screen_width//10,screen_height//12)
        for platform in platforms:
            if heli_rect.colliderect(platform):
                y = y-dy
                dy=0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # if event.type = pygame.K

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -7
                    heading_right = False
                if event.key == pygame.K_RIGHT:
                    dx = 7
                    heading_right = True
                if event.key == pygame.K_UP:
                    flying_up = True
                if event.key == pygame.K_DOWN:
                    dy = 7
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


        # pygame.draw.rect(screen,(100,100,100), heli_rect)
        for platform in platforms:
            pygame.draw.rect(screen, (0,120,0), platform)


        if heading_right:
            screen.blit(heli_right,(x,y))
        else:
            screen.blit(heli_left, (x, y))
        pygame.display.flip()
        clock.tick(25)

    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
