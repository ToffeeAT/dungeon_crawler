import pygame

def draw(screen):
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 64)
    game_over_text = font.render("GAME OVER", True, (255,255,255))
    restart_text = font.render("Press R to restart", True, (255,255,255))
    game_over_rect = game_over_text.get_rect(center=(400,250))
    restart_rect = restart_text.get_rect(center=(400,350))
    screen.blit(game_over_text, game_over_rect)
    screen.blit(restart_text, restart_rect)

def handle_interactions(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            return "RESTART"