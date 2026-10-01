from classes.room import Room
from classes.enemy import Enemy

def save_room_level(room, saved_rooms: dict[str, Room], enemies: list[Enemy], interactables):
    saved_rooms[room] = Room(room, enemies, interactables)


def load_saved_room(room, saved_rooms: dict[str, Room]):
    if room in saved_rooms:
        saved_room = saved_rooms[room]
        enemies = saved_room.enemies
        interactables = saved_room.interactables
        return enemies, interactables

    return None


    