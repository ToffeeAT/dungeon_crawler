import pygame
from functools import lru_cache

def outer_wall_pieces():
    wall_sheet = pygame.image.load(
        "assets/dungeonArt/Set 4.1.png"
    ).convert_alpha()

    # top pieces
    top_left_corner = wall_sheet.subsurface((48, 0, 16, 16))
    top_wall = wall_sheet.subsurface((64, 0, 16, 16))
    top_right_corner = wall_sheet.subsurface((80, 0, 16, 16))

    # side pieces
    left_wall = wall_sheet.subsurface((48, 16, 16, 16))
    right_wall = wall_sheet.subsurface((80, 16, 16, 16))

    # bottom pieces
    bottom_left_corner = wall_sheet.subsurface((48, 32, 16, 16))
    bottom_wall = wall_sheet.subsurface((64, 32, 16, 16))
    bottom_right_corner = wall_sheet.subsurface((80, 32, 16, 16))


    # scale everything by 3
    top_left_corner = pygame.transform.scale_by(top_left_corner, 3)
    top_wall = pygame.transform.scale_by(top_wall, 3)
    top_right_corner = pygame.transform.scale_by(top_right_corner, 3)

    left_wall = pygame.transform.scale_by(left_wall, 3)
    right_wall = pygame.transform.scale_by(right_wall, 3)

    bottom_left_corner = pygame.transform.scale_by(bottom_left_corner, 3)
    bottom_wall = pygame.transform.scale_by(bottom_wall, 3)
    bottom_right_corner = pygame.transform.scale_by(bottom_right_corner, 3)

    return top_left_corner, top_wall, top_right_corner, left_wall, right_wall, bottom_left_corner, bottom_wall, bottom_right_corner
    
def draw_outer_walls(screen, outer_walls):
    top_left_corner, top_wall, top_right_corner, left_wall, right_wall, bottom_left_corner, bottom_wall, bottom_right_corner = outer_wall_pieces()

    wall_size = 48

    for wall in outer_walls:
        if wall.y_pos == 0:
            x = wall.x_pos
            while x < wall.x_pos + wall.width:
                screen.blit(top_wall, (x, 0))
                x += wall_size

        elif wall.y_pos == 560:
            x = wall.x_pos
            while x < wall.x_pos + wall.width:
                screen.blit(bottom_wall, (x, 552))
                x += wall_size

        elif wall.x_pos == 0:
            y = wall.y_pos
            while y < wall.y_pos + wall.height:
                screen.blit(left_wall, (0, y))
                y += wall_size

        else:
            y = wall.y_pos
            while y < wall.y_pos + wall.height:
                screen.blit(right_wall, (752, y))
                y += wall_size

    screen.blit(top_left_corner, (0, 0))
    screen.blit(top_right_corner, (752, 0))
    screen.blit(bottom_left_corner, (0, 552))
    screen.blit(bottom_right_corner, (752, 552))

@lru_cache(maxsize=1)
def structure_pieces():
    structure_sheet = pygame.image.load(
        "assets/dungeonArt/Set 4.04.png"
    ).convert_alpha()

    basic_pillar = structure_sheet.subsurface((80, 16, 16, 48))
    basic_pillar = pygame.transform.scale_by(basic_pillar, 3)

    return {
        "basic_pillar": basic_pillar
    }

def draw_structure(screen, structure, structure_sprites):
    if structure.structure_type in structure_sprites:
        sprite = structure_sprites[structure.structure_type]
        screen.blit(sprite, (structure.x_pos, structure.y_pos))

def get_structure_depth(structure):
    return structure.y_pos + structure.collision_y_offset + structure.collision_height


