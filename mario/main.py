import pygame
from glob import glob
import sys
from pygame.locals import *

pygame.init()
# background = pygame.Surface((640, 400))
# background.fill((30, 90, 120))
# background = pygame.image.load('91cc401f51287f6cde01233e7f01623f-700x400.png')
background = pygame.image.load('game_background_1.png')

# W, H = 640, 400
W, H = 960, 540
HW, HH = W / 2, H / 2
AREA = W * H
FPS = 60
bg_x = 0
isJump = False
jumpCount = 10

clock = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
window = pygame.display.set_mode((W, H))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Sprite, self).__init__()
        self.isJump = False
        self.jumpCount = 10
        self.x = x
        self.y = y
        self.SpriteWalking = glob("Knight/Walking/*.png")
        self.SpriteIdle = glob("Knight/Idle/*.png")
        self.SpriteJump = glob('Knight/JumpALL/0_Fallen_Angels_Jump Loop_005.png')
        self.load_images()

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.rect.x = 50
        self.rect.y = 200


    def load(self, x):
        return pygame.image.load(x).convert_alpha()

    def flip(self, x):
        return pygame.transform.flip(self.load(x), 1, 0)

    def load_images(self):
        self.walkList = [self.load(f) for f in self.SpriteWalking]
        self.walkList_flip = [self.flip(f) for f in self.SpriteWalking]
        self.idleList = [self.load(f) for f in self.SpriteIdle]
        self.idleList_flip = [self.flip(f) for f in self.SpriteIdle]
        self.jumpList = [self.load(f) for f in self.SpriteJump]
        self.counter = 0
        self.image = self.walkList[0]
        self.rect = self.image.get_rect()
        self.dir = ""
        self.prov = ""
        g.add(self)

    def update_counter(self, vel, img_list):
        self.counter += vel
        if self.counter >= len(img_list):
            self.counter = 0
        self.image = img_list[int(self.counter)]

    def update(self):
        if moveRight:
            self.update_counter(.3, self.walkList)
            self.prov = self.dir

        if moveLeft:
            self.update_counter(.1, self.walkList_flip)
            # self.image = self.listflip[int(self.counter)]
            self.prov = self.dir

        if jumpUp:
            self.update_counter(.1, self.jumpList)
            self.prov = self.dir

        if self.dir == "":
            self.update_counter(.1, self.idleList)

            if moveRight:
                self.image = self.idleList[int(self.counter)]

            else:
                self.image = self.idleList_flip[int(self.counter)]

    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def crouch(self):
        crouch_jpg = pygame.image.load('0_Fallen_Angels_Throwing_007.png')
        window.blit(crouch_jpg, (self.x, self.y))


g = pygame.sprite.Group()
# player = Rycerz(50, 200)
player = Sprite(50, 250)
# g.add(player)
moveLeft = False
moveRight = False
jumpUp = False

MOVESPEED = 3


# PRINCESS_jpg = [pygame.image.load('0_Fallen_Angels_Idle Blinking_000.png'), pygame.image.load('0_Fallen_Angels_Idle
# Blinking_001.png'), pygame.image.load('0_Fallen_Angels_Idle Blinking_003.png'), pygame.image.load(
# '0_Fallen_Angels_Idle Blinking_004.png'), pygame.image.load('0_Fallen_Angels_Idle Blinking_005.png'),
# pygame.image.load('0_Fallen_Angels_Idle Blinking_006.png'), pygame.image.load('0_Fallen_Angels_Idle
# Blinking_007.png'), pygame.image.load('0_Fallen_Angels_Idle Blinking_008.png'), pygame.image.load(
# '0_Fallen_Angels_Idle Blinking_009.png'), pygame.image.load('0_Fallen_Angels_Idle Blinking_010.png'),
# pygame.image.load('0_Fallen_Angels_Idle Blinking_011.png'), pygame.image.load('0_Fallen_Angels_Idle
# Blinking_012.png'), pygame.image.load('0_Fallen_Angels_Idle Blinking_013.png'), pygame.image.load(
# '0_Fallen_Angels_Idle Blinking_014.png'), pygame.image.load('0_Fallen_Angels_Idle Blinking_015.png'),
# pygame.image.load('0_Fallen_Angels_Idle Blinking_016.png'), pygame.image.load('0_Fallen_Angels_Idle
# Blinking_017.png')]

# icy_demon1.png

######

# class Mario():
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         # isJump and jumpCount should be attributes of Mario.
#         self.isJump = False
#         self.jumpCount = 10
#
#     # def draw(self):
#     #     # pygame.draw.rect(screen, (255,255,255), (self.x, self.y, 40, 40))
#     #
#     #     if self.isJump:
#     #         window.blit(JUMP_jpg, (self.x, self.y))
#     #         pygame.display.update()
#     #     else:
#     #         window.blit(STAY_jpg, (self.x, self.y, 40, 40))
#     #         pygame.display.update()
#
#     # def update(self):
#     #     # Return to base frame if at end of movement sequence
#     #     if self.move_frame > 6:
#     #         self.move_frame = 0
#     #         return
#
#     def move(self):
#
#         self.move_frame = 0
#         global bg_x
#
#         if self.isJump:
#             JUMP_jpg = pygame.image.load(r'0_Fallen_Angels_Falling Down_003.png')
#             window.blit(JUMP_jpg, (self.x, self.y))
#
#         elif (pressed_keys[K_RIGHT] and bg_x > -920 and self.x < 750) or (
#                 pressed_keys[K_d] and bg_x > -920 and self.x < 750):
#             MOVE_RIGHT_jpg = pygame.image.load(r'0_Fallen_Angels_Running_004.png')
#             window.blit(MOVE_RIGHT_jpg, (self.x, self.y))
#             # if self.x > 490:
#             #     bg_x -= 5
#             # else:
#             self.x += 5
#
#         elif (pressed_keys[K_LEFT] and self.x > 5) or (pressed_keys[K_a] and self.x > 5):
#             MOVE_LEFT_jpg = pygame.image.load(r'0_Fallen_Angels_Running_004-kopia.png')
#             window.blit(MOVE_LEFT_jpg, (self.x, self.y))
#             self.x -= 5
#
#         elif (pressed_keys[K_DOWN]) or (pressed_keys[K_s]):
#             MOVE_DOWN_jpg = pygame.image.load('0_Fallen_Angels_Throwing_007.png')
#             window.blit(MOVE_DOWN_jpg, (self.x, self.y))
#
#         elif pressed_keys[K_SPACE]:
#             # ATTACK = ATTACK_jpg[0]
#             # self.image = ATTACK_jpg[self.move_frame]
#             # pygame.display.update()
#             # window.blit(ATTACK, (self.x, self.y))
#             ATTACK_jpg = pygame.image.load('0_Fallen_Angels_Run Slashing_004.png')
#             window.blit(ATTACK_jpg, (self.x, self.y))
#
#         else:
#             STAY_jpg = pygame.image.load(r'0_Fallen_Angels_Idle_000.png')
#             window.blit(STAY_jpg, (self.x, self.y))
#
#         # if self.isJump:
#         #     if self.jumpCount >= -10:
#         #         neg = 1
#         #         if self.jumpCount < 0:
#         #             neg = -1
#         #         self.y -= self.jumpCount**2 * 0.1 * neg
#         #         self.jumpCount -= 1
#         #     else:
#         #         self.isJump = False
#         #         self.jumpCount = 10
#
#     def jump(self):
#         # Check if mario is jumping and then execute the
#         # jumping code.
#         if self.isJump:
#             if self.jumpCount >= -10:
#                 neg = 1
#                 if self.jumpCount < 0:
#                     neg = -1
#                 self.y -= self.jumpCount ** 2 * 0.1 * neg
#                 self.jumpCount -= 1
#             else:
#                 self.isJump = False
#                 self.jumpCount = 10

######

# class Rycerz(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super(Rycerz, self).__init__()
#         self.x = x
#         self.y = y
#         self.playerwalking = glob("Knight/Walking/*.png")
#         self.playeridle = glob("Knight/Idle/*.png")
#         self.playerjump = pygame.image.load(r'0_Fallen_Angels_Falling Down_003.png')
#         self.load_images()
#         self.isJump = False
#         self.jumpCount = 10
#         self.rect.topleft = [x, y]
#
#
#     def jump(self):
#         # Check if mario is jumping and then execute the
#         # jumping code.
#         if self.isJump:
#             if self.jumpCount >= -10:
#                 neg = 1
#                 if self.jumpCount < 0:
#                     neg = -1
#                 self.y -= self.jumpCount ** 2 * 0.1 * neg
#                 self.jumpCount -= 1
#             else:
#                 self.isJump = False
#                 self.jumpCount = 10
#
#
#
#     def load(self, x):
#         return pygame.image.load(x).convert_alpha()
#
#     def flip(self, x):
#         return pygame.transform.flip(self.load(x), True, False)
#
#     def load_images(self):
#         self.list = [self.load(f) for f in self.playerwalking]
#         self.listflip = [self.flip(f) for f in self.playerwalking]
#         self.list_idle = [self.load(f) for f in self.playeridle]
#         self.list_idleflip = [self.flip(f) for f in self.playeridle]
#         self.counter = 0
#         self.image = self.list[0]
#         self.rect = self.image.get_rect()
#         self.dir = ""
#         self.prov = ""
#         g.add(self)
#
#     def update_counter(self, vel, img_list):
#         self.counter += vel
#         if self.counter >= len(img_list):
#             self.counter = 0
#         self.image = img_list[int(self.counter)]
#
#     def update(self):
#         if moveRight:
#             self.update_counter(.3, self.list)
#             self.prov = self.dir
#
#         if moveLeft:
#             self.update_counter(.1, self.listflip)
#             # self.image = self.listflip[int(self.counter)]
#             self.prov = self.dir
#
#         if self.dir == "":
#             self.update_counter(.1, self.list_idle)
#
#             if moveRight:
#                 self.image = self.list_idle[int(self.counter)]
#
#             else:
#                 self.image = self.list_idleflip[int(self.counter)]


# walking = [pygame.image.load('Walking/0_Ogre_Walking_000.png'), pygame.image.load('Walking/0_Ogre_Walking_002.png'),
#            pygame.image.load('Walking/0_Ogre_Walking_004.png'), pygame.image.load('Walking/0_Ogre_Walking_006.png'), ]

class Ogre():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveEnemy(self):
        # printowanie enemy na ekranie
        walking_jpg = pygame.image.load('Walking/0_Ogre_Walking_001.png')
        window.blit(walking_jpg, (self.x, self.y))
        # enemy idzie w lewo dopoki nie dojdzie do konca mapy
        if self.x > 120:
            self.x -= 0.3

        else:
            walking_jpg = pygame.image.load('0_Ogre_Slashing_005.png')
            window.blit(walking_jpg, (self.x, self.y))

    # def update(self):
    #     # Return to base frame if at end of movement sequence
    #     self.move_frame = 0
    #
    #     # Move the character to the next frame if conditions are met
    #     self.image = walking[self.move_frame]
    #     self.direction = "LEFT"
    #     self.move_frame += 1
    #
    #     # Returns to base frame if standing still and incorrect frame is showing
    #     self.move_frame = 0
    #     self.image = walking[self.move_frame]

    # def Killing(self):
    #     if pygame.key.get_pressed(K_SPACE):
    #         Ogre.update = 0
    #         walking_jpg = pygame.image.load('0_Ogre_Dying_011.png')


class Ogre2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()
        self.walk_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_000.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_002.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_004.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_006.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_008.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_010.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_012.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_014.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_016.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_018.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_020.png'))
        self.sprites.append(pygame.image.load('enemy/Walking/0_Ogre_Walking_022.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.swing_animation = False
        self.ataki = []
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_000.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_001.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_002.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_003.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_004.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_005.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_006.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_007.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_008.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_009.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_010.png'))
        self.ataki.append(pygame.image.load('enemy/Attak/0_Ogre_Slashing_011.png'))
        self.image2 = self.ataki[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

        self.rect.x = 700

        self.speedy = 0.05
        # if x > 120:
        #     x -= 0.3

    def update2(self):
        self.rect.x -= self.speedy
        if self.rect.x == 90:
            self.speedy = 0

    def swingattack(self):
        self.swing_animation = False
        if self.rect.x == 90:
            self.swing_animation = True

    def attack(self):
        self.walk_animation = True
        if self.rect.x == 90:
            self.walk_animation = False

    def update(self, speed):
        if self.walk_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.walk_animation = False

        self.image = self.sprites[int(self.current_sprite)]

    def updateattack(self, speed):
        if self.swing_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.ataki):
                self.current_sprite = 0
                self.swing_animation = False

        self.image2 = self.ataki[int(self.current_sprite)]



class Princess(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_000.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_001.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_002.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_003.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_004.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_005.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_006.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_007.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_008.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_009.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_010.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_011.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_012.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_013.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_014.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_015.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_016.png'))
        self.sprites.append(pygame.image.load('Princess/0_Fallen_Angels_Idle Blinking_017.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def attack(self):
        self.attack_animation = True

    def update(self, speed):
        if self.attack_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]


# mario = Mario(50, 200)
enemy = Ogre(500, 200)
enemy2 = Ogre(650, 200)
enemy3 = Ogre(1000, 200)
# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
princess = Princess(10, 200)
moving_sprites.add(princess)
ogre = Ogre2(650, 200)


moving_sprites.add(ogre)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
                player.image = player.walkList[int(player.counter)]
            if event.key == K_UP or event.key == K_w:
                player.isJump = True
                jumpUp = True
            if event.key == K_DOWN or event.key == K_s:
                player.crouch = True

        # KEYUP

        if event.type == KEYUP:
            player.counter = 0
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                jumpUp = False
            if event.key == K_DOWN or event.key == K_s:
                player.crouch = False

    # Move the player.
    # if player.crouch and player.rect.bottom < H:
    #     player.rect.top += MOVESPEED
    # if player.isJump and player.rect.top > 0:
    #     player.rect.top -= MOVESPEED
    if moveLeft and player.rect.left > -35:
        player.rect.left -= MOVESPEED
        try:
            player.counter += .1
            player.image = pygame.transform.flip(player.walkList[int(player.counter)], True, False)
        except:
            player.counter = 0
            player.image = pygame.transform.flip(player.walkList[int(player.counter)], True, False)
    if moveRight and player.rect.right < W + 35:
        player.rect.right += MOVESPEED
        try:
            player.counter -= .1
            player.image = player.walkList[int(player.counter)]
        except:
            player.counter = 0
            player.image = player.walkList[int(player.counter)]

    # if event.type == KEYDOWN:
    #     # Change the keyboard variables.
    #     if event.key == K_LEFT or event.key == ord('a'):
    #         moveRight = False
    #         moveLeft = True
    #     if event.key == K_RIGHT or event.key == ord('d'):
    #         moveLeft = False
    #         moveRight = True
    #         player.image = player.list[int(player.counter)]
    #     if event.key == pygame.K_UP or event.key == pygame.K_w:
    #         # Start to jump by setting isJump to True.
    #         player.isJump = True
    #         mario.isJump = True
    #         # ANIMACJA SKAKANIA LOAD IMAGE
    #         player.image = player.list_jump[int(player.counter)]
    #
    #     # KEYUP
    #
    # if event.type == KEYUP:
    #     player.counter = 0
    #     if event.key == K_ESCAPE:
    #         pygame.quit()
    #         sys.exit()
    #     if event.key == K_LEFT or event.key == ord('a'):
    #         moveLeft = False
    #     if event.key == K_RIGHT or event.key == ord('d'):
    #         moveRight = False
    #     if event.key == K_UP or event.key == ord('w'):
    #         moveUp = False
    #         player.isJump = False
    #     if event.key == K_DOWN or event.key == ord('s'):
    #         moveDown = False

    # pressed_keys
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    #     moveRight = True
    # elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
    #     moveLeft = True
    # elif keys[pygame.K_UP] or keys[pygame.K_w]:
    #     player.isJump = True
    #     pygame.image.load('0_Fallen_Angels_Falling Down_003.png')
    # elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and keys[pygame.K_UP] or keys[pygame.K_w]:
    #     moveLeft = True
    #     player.isJump = True
    #     pygame.image.load('0_Fallen_Angels_Falling Down_003.png')
    #
    # else:
    #     moveRight = False
    #     moveLeft = False
    #     player.isJump = False
    #
    # # Move the player.
    # if moveLeft and player.rect.left > -35:
    #     player.rect.left -= MOVESPEED
    #     try:
    #         player.counter += .1
    #         player.image = pygame.transform.flip(player.list[int(player.counter)], True, False)
    #     except:
    #         player.counter = 0
    #         player.image = pygame.transform.flip(player.list[int(player.counter)], True, False)
    # if moveRight and player.rect.right < W + 35:
    #     player.rect.right += MOVESPEED
    #     try:
    #         player.counter -= .1
    #         player.image = player.list[int(player.counter)]
    #     except:
    #         player.counter = 0
    #         player.image = player.list[int(player.counter)]

    clock.tick(FPS)
    pressed_keys = pygame.key.get_pressed()
    screen.blit(background, (bg_x, 0))

    moving_sprites.draw(screen)
    moving_sprites.update(0.25)

    princess.attack()
    princess.update(0.05)

    ogre.attack()
    ogre.update(0.05)
    ogre.update2()
    ogre.swingattack()
    ogre.updateattack(0.25)

    # enemy.moveEnemy()
    # enemy2.moveEnemy()
    # enemy3.moveEnemy()

    player.jump()

    # mario.move()
    # mario.draw()
    # mario.jump()

    g.draw(screen)
    g.update()

    # player.jump()

    pygame.display.update()
