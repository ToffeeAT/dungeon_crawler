import pygame
from classes.chest import Chest


inventory_sheet = pygame.image.load("ui_art/PNG/Inventory.png")
chest_panel = inventory_sheet.subsurface((112, 1, 103, 99))
chest_panel = pygame.transform.scale_by(chest_panel, 3)


def draw(screen, chest: Chest, selected_chest_slot):
    screen.fill((0,0,0))
    chest_panel_rect = chest_panel.get_rect(center=(400,300))
    screen.blit(chest_panel, chest_panel_rect)

    first_slot_x = chest_panel_rect.x + 72
    first_slot_y = chest_panel_rect.y + 72

    selected_row = selected_chest_slot // 5
    selected_column = selected_chest_slot % 5
    selected_x = first_slot_x + (selected_column * 48)
    selected_y = first_slot_y + (selected_row * 48)
    selected_rect = pygame.Rect(0, 0, 45, 45)
    selected_rect.center = (selected_x, selected_y)

    pygame.draw.rect(screen, (255,255,255), selected_rect, 3)

    for index, item in enumerate(chest.items):
        row = index // 5
        column = index % 5

        x = first_slot_x + (column * 48)
        y = first_slot_y + (row * 48)

        item_icon = pygame.image.load(item.icon)
        item_icon = pygame.transform.scale_by(item_icon, 3)

        item_rect = item_icon.get_rect(center=(x,y))
        screen.blit(item_icon, item_rect)

def slot_selection(selected_chest_slot, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            if selected_chest_slot < 19:
                selected_chest_slot += 1
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            if selected_chest_slot > 0:
                selected_chest_slot -= 1
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            if selected_chest_slot <= 14:
                selected_chest_slot += 5
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            if selected_chest_slot >= 5:
                selected_chest_slot -= 5

    return selected_chest_slot

