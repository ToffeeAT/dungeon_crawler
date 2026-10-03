import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

floor_colour = (105, 120, 150)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(floor_colour)

    pygame.display.flip()

pygame.quit()