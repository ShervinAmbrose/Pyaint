import pygame
import pygame.gfxdraw
pygame.init()

display = 800
squares = 50
sqrWidth = display // squares
blockx = -1
blocky = -1
screen = pygame.display.set_mode((display, display))
pygame.display.set_caption('PAINT')


def calc(points):
    global blockx, blocky
    blockx = -1
    blocky = -1
    for i in range(display-1):
        if points[0]//sqrWidth == i:
            blockx += 1
    for j in range(display-1):
        if points[1]//sqrWidth == j:
            blocky += 1

    # for event in pygame.event.get():
    #     if event.type == pygame.MOUSEBUTTONUP:
    #         print(click)
    #         click = False
    # color(blockx, blocky)


def draw():
    global click
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                calc(event.pos)
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
                return


def app():
    global click
    click = False
    # global blockx, blocky
    # blockx = 500
    # blocky = 500
    screen.fill((255, 255, 255))
    running = True
    while running:
        grid = []
        coord = []
        for event in pygame.event.get():
            # print(event.type)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                calc(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                print('buttonUP')
                click = False
        # pygame.time.delay(5)

        # click = False
        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONUP:
        #         print('buttonUP')
        #         click = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        for row in range(squares):
            grid.append([])
            coord.append([])
            for column in range(squares):
                # grid[row].append(
                #     pygame.gfxdraw.box(screen, pygame.Rect(column * padding + 1, row * padding + 1, sqrSide, sqrSide), (255, 0, 0, 50)))

                coord[row].append(
                    (column * sqrWidth, row * sqrWidth))
        if click:
            draw()
            # print('block are at: ' + str(blockx) + ', ' + str(blocky))
        pygame.draw.rect(
            screen, (255, 0, 0), (coord[blocky][blockx][0], coord[blocky][blockx][1], sqrWidth, sqrWidth))

        pygame.display.update()
    # print(coord[blockx][blocky])

    pygame.quit()


app()


# def mainScreen():
#     running = True
#     screenFont = pygame.font.SysFont('comicsansms', 40, 1, 1)
#     while running:
#         screen.fill((128, 128, 128))
#         screenLabel = screenFont.render(
#             'Click the mouse button to Paint....', 1, (0, 0, 0))
#         screen.blit(
#             screenLabel, (int(screenL/2 - screenLabel.get_width() / 2), int(screenB / 2)), )
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 app()
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_ESCAPE]:
#             running = False
#     pygame.quit()


# mainScreen()
