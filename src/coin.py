class Coin:

    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.sprite_number = 0
        self.sprites = sprites

    def update_sprite_status(self):
        if self.sprite_number == 5:
            self.sprite_number = 0
        else:
            self.sprite_number += 1


