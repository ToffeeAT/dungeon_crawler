import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.player import Player

from classes.wall import Wall

class Enemy:
    def __init__(self, x_pos, y_pos, health, max_health, speed, attack, detection_range, attack_range, attack_cooldown, last_attack_time):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health = health
        self.max_health = max_health
        self.speed = speed
        self.attack = attack
        self.detection_range = detection_range
        self.attack_range = attack_range
        self.attack_cooldown = attack_cooldown
        self.last_attack_time = last_attack_time

    def distance_from_player(self, player: "Player"):
        a = math.pow((player.x_position - self.x_pos),2)
        b = math.pow((player.y_position - self.y_pos), 2)
        return math.sqrt(a + b)

    def detect_player(self, player: "Player"):
        if self.detection_range > self.distance_from_player(player):
            return True
        else:
            return False

    def chase_player(self, player: "Player", walls: list[Wall]):
        if self.detect_player(player):
            if player.x_position > self.x_pos:
                self.x_pos = self.x_pos + self.speed
                for wall in walls:
                    if self.collidesWith(wall):
                        self.x_pos = self.x_pos - self.speed
                        break

            elif player.x_position < self.x_pos:
                self.x_pos = self.x_pos - self.speed
                for wall in walls:
                    if self.collidesWith(wall):
                        self.x_pos = self.x_pos + self.speed
                        break


            if player.y_position > self.y_pos:
                self.y_pos = self.y_pos + self.speed
                for wall in walls:
                    if self.collidesWith(wall):
                        self.y_pos = self.y_pos - self.speed
                        break

            elif player.y_position < self.y_pos:
                self.y_pos = self.y_pos - self.speed
                for wall in walls:
                    if self.collidesWith(wall):
                        self.y_pos = self.y_pos + self.speed
                        break

    def collidesWith(self, wall: Wall):
        enemy_left = self.x_pos
        enemy_right = self.x_pos + 50
        enemy_top = self.y_pos
        enemy_bottom = self.y_pos + 50

        wall_left = wall.x_pos
        wall_right = wall.x_pos + wall.width
        wall_top = wall.y_pos
        wall_bottom = wall.y_pos + wall.height

        x_overlap = enemy_right > wall_left and enemy_left < wall_right
        y_overlap = enemy_top < wall_bottom and enemy_bottom > wall_top
        return x_overlap and y_overlap

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def player_in_range(self, player: "Player"):
        return self.distance_from_player(player) < self.attack_range

    def attack_player(self, player: "Player", current_time):
        if self.player_in_range(player) and ((current_time - self.last_attack_time) > self.attack_cooldown):
            if player.health > 0 and ((player.health - self.attack >= 0)):
                player.health = player.health - self.attack
            elif player.health > 0 and ((player.health - self.attack < 0)):
                player.health = 0
            self.last_attack_time = current_time

    def health_percentage(self):
        return self.health / self.max_health

