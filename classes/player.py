from classes.wall import Wall
from classes.chest import Chest
from classes.structure import Structure
import math
from classes.door import Door
from typing import TYPE_CHECKING
import pygame

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
        self.interact_range = 100
        self.inventory = []
        self.max_inventory_space = 5
        self.width = 35
        self.height = 40
        self.idle_sheet = pygame.image.load("assets/dungeonArt/DG Asha Character/Blue Asha Idle 32x32.png")
        self.walk_sheet = pygame.image.load("assets/dungeonArt/DG Asha Character/Blue Asha Walk 32x32.png")
        self.animation_speed = 150
        self.last_direction_faced = "FRONT"
        #idle_animation_attributes
        self.idle_front_frames = []
        self.idle_back_frames = []
        self.idle_left_frames = []
        self.idle_right_frames = []
        self.init_frames_front("idle")
        self.init_frames_right("idle")
        self.init_frames_back("idle")
        self.init_frames_left("idle")
        self.idle_frame_index = 0
        self.last_idle_update = 0
        #walk_animation_attributes
        self.walk_front_frames = []
        self.walk_right_frames = []
        self.walk_back_frames = []
        self.walk_left_frames = []
        self.init_frames_front("walk")
        self.init_frames_right("walk")
        self.init_frames_back("walk")
        self.init_frames_left("walk")
        self.walk_frame_index = 0
        self.last_walk_update = 0
        self.is_moving = False

        
        

    def move_up(self, walls: list[Wall], interactables, structures: list[Structure]):
        if self.y_position - self.speed >= 0:
            self.y_position = self.y_position - self.speed
            for s in structures + walls + interactables:
                if self.collidesWith(s):
                    self.y_position = self.y_position + self.speed
                    break
            self.last_direction_faced = "BACK"

    def move_down(self, walls: list[Wall], interactables, structures: list[Structure]):
        if self.y_position + self.speed <= 550:
            self.y_position = self.y_position + self.speed
            for s in structures + walls + interactables:
                if self.collidesWith(s):
                    self.y_position = self.y_position - self.speed
                    break
            self.last_direction_faced = "FRONT"


    def move_left(self, walls: list[Wall], interactables, structures: list[Structure]):
        if self.x_position - self.speed >= 0:
            self.x_position = self.x_position - self.speed
            for s in structures + walls + interactables:
                if self.collidesWith(s):
                    self.x_position = self.x_position + self.speed
                    break
            self.last_direction_faced = "LEFT"

    def move_right(self, walls: list[Wall], interactables, structures: list[Structure]):
        if self.x_position + self.speed <= 750:
            self.x_position = self.x_position + self.speed
            for s in structures + walls + interactables:
                if self.collidesWith(s):
                    self.x_position = self.x_position - self.speed
                    break
            self.last_direction_faced = "RIGHT"

    def collidesWith(self, obstacle):
        player_left = self.x_position + 30
        player_right = player_left + self.width
        player_top = self.y_position + 40
        player_bottom = player_top + self.height

        if isinstance(obstacle, Structure):
            if not obstacle.collision_status:
                return False

            obstacle_left = obstacle.x_pos + obstacle.collision_x_offset
            obstacle_right = obstacle_left + obstacle.collision_width
            obstacle_top = obstacle.y_pos + obstacle.collision_y_offset
            obstacle_bottom = obstacle_top + obstacle.collision_height

        else:
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
        return self.distance_from_interactable(obstacle) < self.interact_range

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

    def init_frames_front(self, sheet):
        if sheet == "idle":
            sheet = self.idle_sheet
            li = self.idle_front_frames
        elif sheet == "walk":
            sheet = self.walk_sheet
            li = self.walk_front_frames
        for i in range(8):
            frame = sheet.subsurface((i * 32, 0, 32, 32))
            frame = pygame.transform.scale_by(frame, 3)
            li.append(frame)

    def init_frames_right(self, sheet):
        if sheet == "idle":
            sheet = self.idle_sheet
            li = self.idle_right_frames
        elif sheet == "walk":
            sheet = self.walk_sheet
            li = self.walk_right_frames
        for i in range(8):
            frame = sheet.subsurface((i * 32, 32, 32, 32))
            frame = pygame.transform.scale_by(frame, 3)
            li.append(frame)

    def init_frames_back(self, sheet):
        if sheet == "idle":
            sheet = self.idle_sheet
            li = self.idle_back_frames
        elif sheet == "walk":
            sheet = self.walk_sheet
            li = self.walk_back_frames
        for i in range(8):
            frame = sheet.subsurface((i * 32, 64, 32, 32))
            frame = pygame.transform.scale_by(frame, 3)
            li.append(frame)

    def init_frames_left(self, sheet):
        if sheet == "idle":
            sheet = self.idle_sheet
            li = self.idle_left_frames
        elif sheet == "walk":
            sheet = self.walk_sheet
            li = self.walk_left_frames

        for i in range(8):
            frame = sheet.subsurface((i * 32, 96, 32, 32))
            frame = pygame.transform.scale_by(frame, 3)
            li.append(frame)
    
    def update_idle_animation(self, current_time):
        if (current_time - self.last_idle_update) >= self.animation_speed:
            if self.idle_frame_index < 7:
                self.idle_frame_index += 1
            else:
                self.idle_frame_index = 0
            self.last_idle_update = current_time

    def update_walk_animation(self, current_time):
        if (current_time - self.last_walk_update) >= self.animation_speed:
            if self.walk_frame_index < 7:
                self.walk_frame_index += 1
            else:
                self.walk_frame_index = 0
            self.last_walk_update = current_time

    



       
    