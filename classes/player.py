from classes.wall import Wall
from classes.chest import Chest
import math
from classes.door import Door
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.enemy import Enemy


class Player:
    def __init__(self, x_position, y_position, health, max_health, speed, attack, attack_range):
        self.x_position = x_position
        self.y_position = y_position
        self.health = health
        self.max_health = max_health
        self.speed = speed
        self.attack = attack
        self.attack_range = attack_range
        self.inventory = []
        self.max_inventory_space = 5

    def move_up(self, walls: list[Wall], doors: list[Door]):
        if self.y_position - self.speed >= 0:
            self.y_position = self.y_position - self.speed
            for wall in walls:
                if self.collidesWith(wall):
                    self.y_position = self.y_position + self.speed
                    break
            for door in doors:
                if self.collidesWith(door):
                    self.y_position = self.y_position + self.speed
                    break

    def move_down(self, walls: list[Wall], doors: list[Door]):
        if self.y_position + self.speed <= 550:
            self.y_position = self.y_position + self.speed
            for wall in walls:
                if self.collidesWith(wall):
                    self.y_position = self.y_position - self.speed
                    break
            for door in doors:
                if self.collidesWith(door):
                    self.y_position = self.y_position - self.speed
                    break


    def move_left(self, walls: list[Wall], doors: list[Door]):
        if self.x_position - self.speed >= 0:
            self.x_position = self.x_position - self.speed
            for wall in walls:
                if self.collidesWith(wall):
                    self.x_position = self.x_position + self.speed
                    break
            for door in doors:
                if self.collidesWith(door):
                    self.x_position = self.x_position + self.speed
                    break

    def move_right(self, walls: list[Wall], doors: list[Door]):
        if self.x_position + self.speed <= 750:
            self.x_position = self.x_position + self.speed
            for wall in walls:
                if self.collidesWith(wall):
                    self.x_position = self.x_position - self.speed
                    break
            for door in doors:
                if self.collidesWith(door):
                    self.x_position = self.x_position - self.speed
                    break

    def collidesWith(self, obstacle):
        player_left = self.x_position
        player_right = self.x_position + 50
        player_top = self.y_position
        player_bottom = self.y_position + 50

        obstacle_left = obstacle.x_pos
        obstacle_right = obstacle.x_pos + obstacle.width
        obstacle_top = obstacle.y_pos
        obstacle_bottom = obstacle.y_pos + obstacle.height

        x_overlap = player_right > obstacle_left and player_left < obstacle_right
        y_overlap = player_top < obstacle_bottom and player_bottom > obstacle_top
        return x_overlap and y_overlap

    def distance_from_enemy(self, enemy: "Enemy"):
        a = math.pow((enemy.x_pos - self.x_position),2)
        b = math.pow((enemy.y_pos - self.y_position), 2)
        return math.sqrt(a + b)

    def enemy_in_range(self, enemy: "Enemy"):
        if self.distance_from_enemy(enemy) < self.attack_range:
            return True
        else:
            return False

    def attack_enemy(self, enemy: "Enemy"):
        if self.enemy_in_range(enemy):
            if enemy.health > 0 and (enemy.health - self.attack >= 0):
                enemy.health = enemy.health - self.attack
            elif enemy.health > 0 and (enemy.health - self.attack < 0):
                enemy.health = 0

    def health_percentage(self):
        return self.health / self.max_health

    def distance_from_interactable(self, obstacle):
        a = math.pow((obstacle.x_pos - self.x_position),2)
        b = math.pow((obstacle.y_pos - self.y_position), 2)
        return math.sqrt(a + b)

    def interactable_in_range(self, obstacle):
        return self.distance_from_interactable(obstacle) < self.attack_range

    def interact_with_interactable(self, interactable):
        if self.interactable_in_range(interactable):
            if isinstance(interactable, Door):
                return interactable.connected_room, interactable.x_spawn, interactable.y_spawn
            if isinstance(interactable, Chest):
                return interactable.items, interactable.requires_key

    def is_player_alive(self):
        return self.health > 0

    def is_inventory_full(self):
        return len(self.inventory) >= self.max_inventory_space

    def add_item_to_inventory(self, item):
        if not self.is_inventory_full():
            self.inventory.append(item)

       
    