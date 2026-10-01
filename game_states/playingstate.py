from classes.player import Player
from classes.door import Door
import pygame
import levelload
import statelevelload

def handle_interactions(player: Player, saved_rooms: dict, event, current_room, walls, enemies, interactables):
    if player.is_player_alive():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for enemy in enemies:
                    player.attack_enemy(enemy)
            elif event.key == pygame.K_e:
                for interactable in interactables:
                    if isinstance(interactable, Door):
                        res = player.interact_with_interactable(interactable)
                        if res is not None:
                            new_room, x_spawn, y_spawn = res
                            statelevelload.save_room_level(
                                current_room,
                                saved_rooms,
                                enemies,
                                interactables
                            )
                            current_room = new_room
                            if new_room not in saved_rooms:
                                walls, enemies, interactables = levelload.load_room(new_room)
                            else:
                                enemies, interactables = statelevelload.load_saved_room(
                                    new_room,
                                    saved_rooms
                                )
                                walls = levelload.load_walls(new_room)
                            player.x_position = x_spawn
                            player.y_position = y_spawn

    return current_room, walls, enemies, interactables


def handle_movement(player: Player, walls, interactables):
    keys = pygame.key.get_pressed()
    if player.is_player_alive():
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.move_up(walls, interactables)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.move_down(walls, interactables)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.move_right(walls, interactables)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.move_left(walls, interactables)


def draw(screen, player, walls, enemies, interactables):
    screen.fill((0,0,0))

    for wall in walls:
        pygame.draw.rect(screen, (255,255,255), (wall.x_pos, wall.y_pos, wall.width, wall.height))

    for interactable in interactables:
        if isinstance(interactable, Door):
            pygame.draw.rect(screen, (255,255,0), (interactable.x_pos, interactable.y_pos, interactable.width, interactable.height))

    if player.is_player_alive():
        pygame.draw.rect(screen, (255,0,0), (player.x_position, player.y_position, 50,50))
        pygame.draw.rect(screen, (100,0,0), (player.x_position, player.y_position -10, 50, 6))
        player_health_width = int(50 * player.health_percentage())
        pygame.draw.rect(screen, (0,255,0), (player.x_position, player.y_position -10, player_health_width, 6))

    for enemy in enemies:
        if enemy.is_alive():
            pygame.draw.rect(screen, (0,0,255), (enemy.x_pos, enemy.y_pos, 50,50))
            enemy_health_width = int(50 * enemy.health_percentage())
            pygame.draw.rect(screen, (100,0,0), (enemy.x_pos, enemy.y_pos -10, 50, 6))
            pygame.draw.rect(screen, (0,255,0), (enemy.x_pos, enemy.y_pos -10, enemy_health_width, 6))


def set_enemy_ai(player, enemies, walls, current_time):
    for enemy in enemies:
        if enemy.is_alive() and player.is_player_alive():
            enemy.chase_player(player, walls)
            enemy.attack_player(player, current_time)

def check_current_state(player: Player, current_state):
    if current_state == "PLAYING" and not player.is_player_alive():
        current_state = "GAME_OVER"
    return current_state