import pygame
import pygame.locals
import os
from player import Player
from constants import *


def init_pygame():
    pygame.init()
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_CAPTION)
    return win, clock


def load_images(image_names):
    """
    Load images from list of image names
    :param image_names: names of the images with file extension
    :return:
    """

    images = []
    for image_name in image_names:
        images.append(pygame.image.load(os.path.join('../res/img', image_name)))

    return images


def redraw_game_window(window, background, player):
    global walk_count
    window.blit(background, (0, 0))

    if player.walk_count + 1 >= 9:
        player.walk_count = 0

    if player.left:
        window.blit(player.walk_left_sprites[player.walk_count], (player.x, player.y))
        player.walk_count += 1
    elif player.right:
        window.blit(player.walk_right_sprites[player.walk_count], (player.x, player.y))
        player.walk_count += 1
    else:
        window.blit(player.sprite, (player.x, player.y))

    pygame.display.update()


def main():
    win, clock = init_pygame()
    clock.tick(60)
    background = pygame.image.load(os.path.join('../res/img', 'bg.jpg'))
    player = Player(100, WINDOW_HEIGHT - 145,
                    pygame.image.load(os.path.join('../res/img', 'standing.png')),
                    load_images(PLAYER_LEFT_SPRITE_FILENAMES),
                    load_images(PLAYER_RIGHT_SPRITE_FILENAMES))
    run = True
    while run:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        player.move(keys)


        redraw_game_window(win, background, player)

    pygame.quit()


if __name__ == '__main__':
    main()