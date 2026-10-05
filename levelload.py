from classes.player import Player
from classes.enemy import Enemy
from classes.wall import Wall
from classes.door import Door
from classes.chest import Chest
from classes.item import Item
import json



def create_player():
    return Player(200,300,20,20,3,3,75)

def create_enemies(room_data):
    enemies_objs = []

    with open("data/enemies.json", "r") as file:
        enemy_data = json.load(file)

    enemies_to_create = room_data.get("enemies", [])

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

def create_outerwalls(room_data):
    outer_walls = []
    room_type = room_data["room_layout"]
    with open(f"data/room_layouts/{room_type}.json", "r") as file:
        outer_wall_data = json.load(file)
    for wall in outer_wall_data["walls"]:
        outer_walls.append(Wall(wall["x"], wall["y"], wall["width"], wall["height"]))
    return outer_walls






def create_doors(room_data, interactables):
    door_data = room_data.get("doors", [])
    for door in door_data:
        interactables.append(Door(door["x"], door["y"], door["width"], door["height"], door["connected_room"], door["x_spawn"], door["y_spawn"]))


def create_chests(room_data, interactables):
    chest_data = room_data.get("chests", [])
    with open("data/items.json", "r") as file:
        item_data = json.load(file)
    for chest in chest_data:
        items = []
        for item in chest["items"]:
            data = item_data[item]
            items.append(Item(data["name"], data["description"], data["icon"]))
        interactables.append(Chest(chest["x"], chest["y"], chest["width"], chest["height"], items, chest["requires_key"]))


def load_room(room):
    with open(f"data/rooms/{room}.json", "r") as file:
        room_data = json.load(file)
    walls = create_walls(room_data)
    outer_walls = create_outerwalls(room_data)
    enemies = create_enemies(room_data)
    interactables = interactable_list(room_data)
    return walls, outer_walls, enemies, interactables

def interactable_list(room_data):
    interactables = []
    create_doors(room_data, interactables)
    create_chests(room_data, interactables)
    return interactables

def load_walls(room):
    with open(f"data/rooms/{room}.json", "r") as file:
        room_data = json.load(file)

    return create_walls(room_data)

def load_outer_walls(room):
    with open(f"data/rooms/{room}.json", "r") as file:
        room_data = json.load(file)

    return create_outerwalls(room_data)

