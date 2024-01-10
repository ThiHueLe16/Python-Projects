# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
import os
import random
import math
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5
MAX_HEALTH = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


# load image and split the image of the main charater
def load_sprite_sheet(dir1, dir2, width, height, direction=False):
    path = join("venv", "Assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]
    all_sprites = {}
    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites
    return all_sprites


def get_block(size):
    path = join("venv", "Assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)  # 96 is where our block pixel is in the picture
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Player(pygame.sprite.Sprite):  # sprite for perfekt pixel collision ,  handle collision
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheet("MainCharacters", "PinkMan", 32, 32, True)
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)  # eady to move, handle collision
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0  # for jump
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.health = MAX_HEALTH

    def jump(self):
        self.y_vel = -self.GRAVITY * 8  # set speed of jump
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):  # move player
        # add to y_vel to keep the player move down when jump
        # add grativity
        # add accelebration
        self.y_vel += min(1, (
                self.fall_count / fps) * self.GRAVITY)  # for every frame should have at move atleast one pixel

        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1  # constantly add gravity to player
        if self.hit:
            self.hit_count += 1
        if self.hit and self.hit_count==FPS:
            self.health -= 1
        if self.hit_count > fps * 2:  # 2 second
            self.hit = False
            self.hit_count = 0

        self.update_sprite()  # update movement animation of player

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.fall_count = 0
        self.y_vel *= -1

    def make_hit(self):
        self.hit = True
        self.hit_count += 1
        if self.hit_count == 120:
            self.health -= 1

    def update_sprite(self):  # for the movement animation of the player
        sprite_sheet = "idle"
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def health_bar(self, window, offset_x):
        pygame.draw.rect(window, (255, 0, 0), (self.rect.x - offset_x, self.rect.top - 20, 70, 10))
        pygame.draw.rect(window, (0, 255, 0),
                         (self.rect.x - offset_x, self.rect.top - 20, (self.health / MAX_HEALTH) * 70, 10))

    def draw(self, win, offset_x):
        # pygame.draw.rect(win, self.COLOR, self.rect)
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))
        self.health_bar(window, offset_x)


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name="None"):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheet("Traps", "Fire", width, height)  # sprite,present all fire animati
        self.image = self.fire["on"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = 'off'
        self.fire_on_time = 0
        self.is_on = False

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):  # same as update sprite sheet in player

        self.fire_on_time += 1

        if FPS * 2 < self.fire_on_time < FPS * 6:
            self.on()
            self.is_on = True
        if self.fire_on_time == FPS * 6:
            self.off()
            self.fire_on_time = 0
            self.is_on = False

        fire_all_image = self.fire[self.animation_name]
        image_index = (self.animation_count // self.ANIMATION_DELAY) % len(fire_all_image)
        self.image = fire_all_image[image_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        # important for static not move object to set animation count back t0 0 so it not big big in future

        if self.animation_count // self.ANIMATION_DELAY > len(fire_all_image):
            self.animation_count = 0


def get_background(name):
    image = pygame.image.load(os.path.join("venv", "Assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    for i in range(WIDTH // width + 1):  # how mayny tile need to fill the screen
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)
    for obj in objects:
        obj.draw(window, offset_x)
    player.draw(window, offset_x)
    pygame.display.update()


def handle_vertical_collision(player, objects, dy):
    collide_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:  # moving down
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:  # moving up
                player.rect.top = obj.rect.bottom
                player.hit_head()
            collide_objects.append(obj)
    return collide_objects


# handle collision horizontal

def collide(player, objects, dx):
    player.move(dx, 0)  # check if they would collide the object left or right if they move
    player.update()  # update the mask
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)  # move them back tp original place
    player.update()  # uodate the mask
    return collided_object


def handle_move(player, objects):
    keys = pygame.key.get_pressed()
    player.x_vel = 0  # set back so that player doesnt keep going forever

    collide_left = collide(player, objects,
                           -PLAYER_VEL * 2)  # *2 TO FIX THE problem of collide because sprite can ship the picture abit to left or right

    collide_right = collide(player, objects, PLAYER_VEL * 2)

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VEL)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    check_collide = [collide_left, collide_right, *vertical_collide]

    for obj in check_collide:
        if obj and obj.name == "fire" and obj.is_on:
            player.make_hit()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Yellow.png")
    player = Player(700, 100, 50, 50)
    block_size = 96
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in
             range(-WIDTH // block_size, WIDTH * 2 // block_size)]
    floor1=[Block(-1392 - 96*i, HEIGHT - block_size, block_size) for i in range(3,20)]
    wall=[Block(WIDTH- block_size, HEIGHT - block_size*i, block_size) for i in
             range(2,HEIGHT// block_size +2)]

    # fire = [Fire(i * random.randint(1, 1000), HEIGHT - block_size - 64, 16, 32) for i in
    #        range(random.randint(1, 1000))]
    fire = [Fire(100, HEIGHT - block_size - 64, 16, 32),
            Fire(132, HEIGHT - block_size - 64, 16, 32),
            Fire(block_size * 3 + 32, HEIGHT - block_size * 4 - 64, 16, 32),
            Fire(-600 + 40, HEIGHT - block_size * 4 - 64, 16, 32),
            Fire(-400 + 40, HEIGHT - block_size * 2 - 64, 16, 32),
            Fire(-1059 + 96, HEIGHT - block_size * 2 + 32, 16, 32)]
    objects = [*floor,
               *floor1,
               *wall,
               Block(0, HEIGHT - block_size * 2, block_size),
               Block(block_size * 3, HEIGHT - block_size * 4, block_size),
               Block(-96, HEIGHT - block_size * 2, block_size),
               Block(-400, HEIGHT - block_size * 2, block_size),
               Block(-600, HEIGHT - block_size * 4, block_size),
               Block(-700, HEIGHT - block_size * 3, block_size),
               Block(-1059, HEIGHT - block_size * 2, block_size),
               Block(-1200, HEIGHT - block_size * 3, block_size),
               Block(-1296, HEIGHT - block_size * 3, block_size),
               Block(-1392, HEIGHT - block_size * 3, block_size),
               *fire
               ]
    # blocks=[Block(0,HEIGHT-block_size, block_size)]
    offset_x = 0  # for scolling the floor
    scroll_area_width = 200
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
        player.loop(FPS)  # move the player
        for f in fire:  # loop the fire
            f.loop()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x)

        # scrolling the floor
        if (player.rect.right - offset_x >= WIDTH - scroll_area_width and player.x_vel > 0) or (
                (player.rect.left - offset_x <= WIDTH - scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
