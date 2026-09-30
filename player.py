from wall import Wall
import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from enemy import Enemy


class Player:
    def __init__(self, x_position, y_position, health, max_health, speed, attack, attack_range):
        self.x_position = x_position
        self.y_position = y_position
        self.health = health
        self.max_health = max_health
        self.speed = speed
        self.attack = attack
        self.attack_range = attack_range

    def move_up(self, walls: list[Wall]):
        if self.y_position - self.speed >= 0:
            self.y_position = self.y_position - self.speed
            for wall in walls:
                if self.collidesWith(wall):
                    self.y_position = self.y_position + self.speed
                    break

    def move_down(self, walls: list[Wall]):
        if self.y_position + self.speed <= 550:
            self.y_position = self.y_position + self.speed
            for wall in walls:
                if self.collidesWith(wall):
                    self.y_position = self.y_position - self.speed
                    break


    def move_left(self, walls: list[Wall]):
        if self.x_position - self.speed >= 0:
            self.x_position = self.x_position - self.speed
            for wall in walls:
                if self.collidesWith(wall):
                    self.x_position = self.x_position + self.speed
                    break

    def move_right(self, walls: list[Wall]):
        if self.x_position + self.speed <= 750:
            self.x_position = self.x_position + self.speed
            for wall in walls:
                if self.collidesWith(wall):
                    self.x_position = self.x_position - self.speed
                    break

    def collidesWith(self, wall: Wall):
        player_left = self.x_position
        player_right = self.x_position + 50
        player_top = self.y_position
        player_bottom = self.y_position + 50

        wall_left = wall.x_pos
        wall_right = wall.x_pos + wall.width
        wall_top = wall.y_pos
        wall_bottom = wall.y_pos + wall.height

        x_overlap = player_right > wall_left and player_left < wall_right
        y_overlap = player_top < wall_bottom and player_bottom > wall_top
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


    