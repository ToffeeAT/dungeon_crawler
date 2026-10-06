class Structure:
    def __init__(self, x_pos, y_pos, width, height, structure_type, collision_status, collision_x_offset, collision_y_offset, collision_width, collision_height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.structure_type = structure_type
        self.collision_status = collision_status
        self.collision_x_offset = collision_x_offset
        self.collision_y_offset = collision_y_offset
        self.collision_width = collision_width
        self.collision_height = collision_height