from graham_scan.solve1 import graham_scan_1
from graham_scan.solve2 import graham_scan_2
from monotone_chain.solve import monotone_chain
from jarvis_march.solve import jarvis_march
from quick_hull.solve import quick_hull

algorithms = [graham_scan_1, graham_scan_2, monotone_chain, jarvis_march, quick_hull]
number_algorithm = 4

try:
    import pygame
    from pygame.color import *
    from pygame.locals import *

    pygame.init()

    caption = 'Visualization for convex hulls'
    resolution = (600, 600)
    text = ['Click mouse to draw dots',
            'Press <Space> to reset',
            'Press <Esc> to exit']

    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption(caption)
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 20)

    coords = []
    segments = []
    running = True

    while running:
        # events handling
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                coords.append(event.pos)
                if len(coords) >= 3:
                    segments = algorithms[number_algorithm](coords)
                    print segments
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    segments = []
                    coords = []
                elif event.key == K_ESCAPE:
                    running = False

        # fill screen
        screen.fill(Color('white'))

        # draw help text
        y = 5
        for line in text:
            img = font.render(line, 1, Color('black'))
            screen.blit(img, (5, y))
            y += 15

        # draw dots
        for coord in coords:
            pygame.draw.circle(screen, Color('blue'), coord, 2, 0)

        # draw segments
        if len(coords) >= 3:
            pygame.draw.lines(screen, Color('grey'), True, segments, 2)

        # step
        pygame.display.update()
        clock.tick(50)

except ImportError:
    print 'Unable to import pygame'
