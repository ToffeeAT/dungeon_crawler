import pygame
import levelload
import game_states.playingstate as playingstate
import game_states.gameoverstate as gameoverstate
import game_states.cheststate as cheststate

pygame.init()

def start_game():
    saved_rooms = {}
    current_room = "room1"
    player = levelload.create_player()
    walls, enemies, interactables = levelload.load_room("room1")
    current_state = "PLAYING"
    return saved_rooms, current_room, player, walls, enemies, interactables, current_state

saved_rooms, current_room, player, walls, enemies, interactables, current_state = start_game()
active_chest = None
selected_chest_slot = 0

screen = pygame.display.set_mode((800,600))

running = True
clock = pygame.time.Clock()

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if current_state == "PLAYING":
            current_room, walls, enemies, interactables, active_chest = playingstate.handle_interactions(player, saved_rooms, event, current_room, walls, enemies, interactables)
            if active_chest is not None:
                current_state = "CHEST"

        if current_state == "GAME_OVER":
            res = gameoverstate.handle_interactions(event)
            if res == "RESTART":
                saved_rooms, current_room, player, walls, enemies, interactables, current_state = start_game()

        if current_state == "CHEST":
            selected_chest_slot = cheststate.slot_selection( selected_chest_slot, event)

    if current_state == "PLAYING":
        current_state = playingstate.check_current_state(player, current_state)
        playingstate.handle_movement(player, walls, interactables)
        if player.is_moving == True:
            player.update_walk_animation(current_time)
        else:
            player.update_idle_animation(current_time)
        playingstate.set_enemy_ai(player, enemies, walls, current_time)
        playingstate.draw(screen, player, walls, enemies, interactables)
    elif current_state == "GAME_OVER":
        gameoverstate.draw(screen)
    elif current_state == "CHEST":
        cheststate.draw(screen, active_chest, selected_chest_slot)


    pygame.display.flip()

    clock.tick(60)
