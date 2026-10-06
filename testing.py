import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pillar Hitbox Testing")

clock = pygame.time.Clock()

pillar_sheet = pygame.image.load(
    "assets/dungeonArt/Set 4.04.png"
).convert_alpha()

# intact pillar
pillar = pillar_sheet.subsurface(80, 16, 16, 48)

# scale x3
pillar_big = pygame.transform.scale_by(pillar, 3)

pillar_x = 300
pillar_y = 150

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 40, 40))

    # draw pillar
    screen.blit(pillar_big, (pillar_x, pillar_y))

    # temporary hitbox
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (
            pillar_x,
            pillar_y + 112,
            48,
            24
        ),
        2
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()