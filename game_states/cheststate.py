import pygame
from classes.chest import Chest


inventory_sheet = pygame.image.load("ui_art/PNG/Inventory.png")
chest_panel = inventory_sheet.subsurface((112, 1, 103, 99))
chest_panel = pygame.transform.scale_by(chest_panel, 3)

def draw(screen, chest: Chest):
    screen.fill((0,0,0))
    chest_panel_rect = chest_panel.get_rect(center=(400,300))
    screen.blit(chest_panel, chest_panel_rect)