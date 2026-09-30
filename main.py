from player import Player
from wall import Wall
from enemy import Enemy
from door import Door
import pygame
import levelload

pygame.init()



player = levelload.create_player()
walls, enemies, interactables = levelload.load_room("room1")


screen = pygame.display.set_mode((800,600))

running = True
clock = pygame.time.Clock()
while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for enemy in enemies:
                    player.attack_enemy(enemy)
            elif event.key == pygame.K_e:
                for interactable in interactables:
                    if isinstance(interactable, Door):
                        res = player.interact_with_interactable(interactable)
                        if res is not None:
                            print(res)
                            new_room, x_spawn, y_spawn = res
                            walls, enemies, interactables = levelload.load_room(new_room)
                            player.x_position = x_spawn
                            player.y_position = y_spawn
                            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.move_up(walls, interactables)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.move_down(walls, interactables)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_right(walls, interactables)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_left(walls, interactables)

    for enemy in enemies:
        if enemy.is_alive():
            enemy.chase_player(player, walls)
            enemy.attack_player(player, current_time)
    
    screen.fill((0,0,0))

    for wall in walls:
        pygame.draw.rect(screen, (255,255,255), (wall.x_pos, wall.y_pos, wall.width, wall.height))

    for interactable in interactables:
        if isinstance(interactable, Door):
            pygame.draw.rect(screen, (255,255,0), (interactable.x_pos, interactable.y_pos, interactable.width, interactable.height))

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


    pygame.display.flip()
    

    clock.tick(60)

