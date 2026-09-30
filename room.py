from enemy import Enemy

class Room:
    def __init__(self,room_name, enemies: list[Enemy], interactables):
        self.room_name = room_name
        self.enemies = enemies
        self.interactables = interactables