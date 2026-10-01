import pygame

def draw(screen):
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 64)
    game_over_text = font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over_text, (250,250))