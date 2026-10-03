
class Chest:
    def __init__(self, x_pos, y_pos, width, height, items, requires_key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.items = items
        self.requires_key = requires_key