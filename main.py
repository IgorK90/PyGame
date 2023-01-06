import pygame


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((700,500))
    pygame.display.set_caption("Heli")
    clock= pygame.time.Clock()

    x= 500
    y = 100
    heli = pygame.image.load("heli_right.png")
    heli = pygame.transform.scale(heli,(64,64))

    background = pygame.image.load("plx-5.png")
    background = pygame.transform.scale(background,(700,500))

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = x-10
                if event.key == pygame.K_RIGHT:
                    x = x+10
                if event.key == pygame.K_UP:
                    y = y-10
                if event.key == pygame.K_DOWN:
                    y = y+10

        screen.fill((255,255,255))
        screen.blit(background,(0,0))
        screen.blit(heli,(x,y))
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
