from constants import DEFAULT_PLAYER_SPEED
import pygame


class Player:
    """
    Player class
    """
    def __init__(self, x, y, sprite, walk_left_sprites, walk_right_sprites, vel=None):
        """
        Initialize player with an x and y position.
        :param x: x position
        :param y: y position
        :param vel: speed of player
        """
        self.x = x
        self.y = y
        self.left = False
        self.right = False
        self.walk_count = 0
        if vel is None: self.vel = DEFAULT_PLAYER_SPEED
        self.sprite = sprite
        self.walk_left_sprites = walk_left_sprites
        self.walk_right_sprites = walk_right_sprites

    def move(self, keys):
        """
        Move the player.
        :param keys: List of key presses.
        :return:
        """
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.left = True
            self.right = False
        elif keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.left = False
            self.right = True
        elif keys[pygame.K_UP]:
            self.y -= self.vel
        elif keys[pygame.K_DOWN]:
            self.y += self.vel
        else:
            self.right = False
            self.left = False
            self.walk_count = 0
