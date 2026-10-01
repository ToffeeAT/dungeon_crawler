from classes.player import Player
from classes.wall import Wall
from classes.enemy import Enemy
from classes.door import Door
import pygame
import levelload
import statelevelload
import game_states.playingstate as playingstate
import game_states.gameoverstate as gameoverstate

pygame.init()


saved_rooms = {}
current_room = "room1"
player = levelload.create_player()
walls, enemies, interactables = levelload.load_room("room1")
current_state = "PLAYING"

screen = pygame.display.set_mode((800,600))

running = True
clock = pygame.time.Clock()

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if current_state == "PLAYING":
            current_room, walls, enemies, interactables = playingstate.handle_interactions(player, saved_rooms, event, current_room, walls, enemies, interactables)

    if current_state == "PLAYING":
        current_state = playingstate.check_current_state(player, current_state)
        playingstate.handle_movement(player, walls, interactables)
        playingstate.set_enemy_ai(player, enemies, walls, current_time)
        playingstate.draw(screen, player, walls, enemies, interactables)
    elif current_state == "GAME_OVER":
        gameoverstate.draw(screen)

    pygame.display.flip()

    clock.tick(60)
