import pygame

if __name__ == '__main__':
    pygame.init()
    size = (700, 500)
    screen_width = size[0]
    screen_height = size[1]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Heli")
    clock = pygame.time.Clock()

    heli_right = pygame.image.load("heli_right.png")
    heli_right = pygame.transform.scale(heli_right, (screen_width // 10, screen_width // 10))

    heli_left = pygame.image.load("heli_left.png")
    heli_left = pygame.transform.scale(heli_left, (screen_width // 10, screen_width // 10))

    background = pygame.image.load("plx-5.png")
    background = pygame.transform.scale(background, (700, 500))

    x = screen_width // 2 - screen_width // 20
    y = screen_height // 2 - screen_width // 20

    dx = 0
    dy = 0
    flying_up = False
    heading_right = True

    background_x = 0

    level = [[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,],
             [1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,],
             [1,0,0,7,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
             [1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,],
             [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,],
             [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,],
             [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
             [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
             [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
             [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
             ]
    platforms = list()
    brick_size= size[1]//11
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j]==1:
                platforms.append(pygame.Rect(j*brick_size, i*brick_size, brick_size,brick_size))
            if level[i][j]==7:
                x,y = j*brick_size, i*brick_size



    # platforms = [pygame.Rect(0, 0, 40, 500),
    #              pygame.Rect(0, 450, 500, 40),
    #              pygame.Rect(100, 100, 300, 40),
    #              pygame.Rect(500, 200, 100, 40), ]

    game_over = False
    while not game_over:
        if flying_up:
            dy = dy - 1
            if dy < -10:
                dy = -10
        else:
            dy = dy + 0.5
            if dy > 10:
                dy = 10

        x = x + dx
        heli_rect = pygame.Rect(x, y, screen_width // 10, screen_width // 12)
        for platform in platforms:
            if heli_rect.colliderect(platform):
                x = x - dx

        y = y + dy
        heli_rect = pygame.Rect(x, y, screen_width // 10, screen_width // 12)
        for platform in platforms:
            if heli_rect.colliderect(platform):
                y = y - dy
                dy = 0

        if x + background_x > size[0] * 3 / 4:
            background_x = size[0] * 3 / 4 - x

        if x + background_x < size[0] * 1 / 4:
            background_x = size[0] * 1 / 4 - x

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
                    if dx < 0:
                        dx = 0
                if event.key == pygame.K_RIGHT:
                    if dx > 0:
                        dx = 0
                if event.key == pygame.K_UP:
                    flying_up = False
                if event.key == pygame.K_DOWN:
                    if dy > 0:
                        dy = 0

        screen.fill((255, 255, 255))
        screen.blit(background, (background_x % size[0], 0))
        screen.blit(background, (background_x % size[0] - size[0], 0))

        # pygame.draw.rect(screen,(100,100,100), heli_rect)
        for platform in platforms:
            pygame.draw.rect(screen, (0, 120, 0),
                             (platform.x + background_x, platform.y, platform.width, platform.height))

        if heading_right:
            screen.blit(heli_right, (x + background_x, y))
        else:
            screen.blit(heli_left, (x + background_x, y))
        pygame.display.flip()
        clock.tick(25)

    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
