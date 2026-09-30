from player import Player
from enemy import Enemy
from wall import Wall
from door import Door
import json



def create_player():
    return Player(200,300,20,20,3,3,75)

def create_enemies(room_data):
    enemies_objs = []

    with open("data/enemies.json", "r") as file:
        enemy_data = json.load(file)

    enemies_to_create = room_data["enemies"]

    for enemy in enemies_to_create:
        enemy_type = enemy["type"]
        stats = enemy_data[enemy_type]

        enemies_objs.append(
            Enemy(
                enemy["x"],
                enemy["y"],
                stats["health"],
                stats["max_health"],
                stats["speed"],
                stats["attack"],
                stats["detection_range"],
                stats["attack_range"],
                stats["attack_cooldown"],
                0
            )
        )

    return enemies_objs

def create_walls(room_data):
    walls = []
    wall_data = room_data["walls"]
    for wall in wall_data:
        walls.append(Wall(wall["x"], wall["y"], wall["width"], wall["height"]))
    return walls

def create_doors(room_data, interactables):
    door_data = room_data["doors"]
    for door in door_data:
        interactables.append(Door(door["x"], door["y"], door["width"], door["height"], door["connected_room"], door["x_spawn"], door["y_spawn"]))

def load_room(room):
    with open(f"data/rooms/{room}.json", "r") as file:
        room_data = json.load(file)
    walls = create_walls(room_data)
    enemies = create_enemies(room_data)
    interactables = interactable_list(room_data)
    return walls, enemies, interactables

def interactable_list(room_data):
    interactables = []
    create_doors(room_data, interactables)
    # need moree interactables
    return interactables
