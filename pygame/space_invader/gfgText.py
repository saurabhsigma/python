# import pygame
# import random
# import math
# from pygame import mixer

# # Initialize pygame
# pygame.init()

# # Screen setup
# win_width = 800
# win_height = 600
# window = pygame.display.set_mode((win_width, win_height))

# # Title and icon
# pygame.display.set_caption("Alien Blaster")

# # Score settings
# current_score = 0
# score_pos_x = 10
# score_pos_y = 10
# score_font = pygame.font.Font('freesansbold.ttf', 20)

# # Game Over text
# end_game_font = pygame.font.Font('freesansbold.ttf', 64)

# def display_score(x, y):
#     score_text = score_font.render("Score: " + str(current_score), True, (255, 255, 255))
#     window.blit(score_text, (x, y))

# def display_game_over():
#     over_text = end_game_font.render("GAME OVER", True, (255, 255, 255))
#     window.blit(over_text, (200, 250))

# # Background music
# mixer.music.load('background.mp3')
# mixer.music.play(-1)

# # Player setup
# player_img = pygame.image.load('spaceship.png')
# player_img = pygame.transform.scale(player_img, (64, 64))
# player_x = 370
# player_y = 525
# player_change_x = 0

# # Enemy setup
# enemy_images = []
# enemy_x = []
# enemy_y = []
# enemy_change_x = []
# enemy_change_y = []
# enemy_count = 8

# for _ in range(enemy_count):
#     enemy_images.append(pygame.image.load('alien.png'))
#     enemy_images[-1] = pygame.transform.scale(enemy_images[-1], (64, 64))
#     enemy_x.append(random.randint(50, 750))
#     enemy_y.append(random.randint(30, 150))
#     enemy_change_x.append(0.3)
#     enemy_change_y.append(40)

# # Bullet setup
# bullet_img = pygame.image.load('bullet.png')
# bullet_img = pygame.transform.scale(bullet_img, (32, 64))
# bullet_x = 0
# bullet_y = player_y
# bullet_change_y = 4
# bullet_active = False

# # Collision detection
# def check_collision(obj1_x, obj2_x, obj1_y, obj2_y):
#     distance = math.sqrt((math.pow(obj1_x - obj2_x, 2)) + (math.pow(obj1_y - obj2_y, 2)))
#     return distance <= 50

# # Player movement
# def draw_player(x, y):
#     window.blit(player_img, (x, y))

# # Enemy rendering
# def draw_enemy(x, y, idx):
#     window.blit(enemy_images[idx], (x, y))

# # Bullet movement
# def fire_bullet(x, y):
#     global bullet_active
#     bullet_active = True
#     window.blit(bullet_img, (x, y))

# # Game loop
# run_game = True
# while run_game:
#     window.fill((0, 0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run_game = False

#         # Player control
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 player_change_x = -1.7
#             if event.key == pygame.K_RIGHT:
#                 player_change_x = 1.7
#             if event.key == pygame.K_SPACE:
#                 if not bullet_active:
#                     bullet_x = player_x + 16
#                     fire_bullet(bullet_x, bullet_y)
#                     shot_sound = mixer.Sound('bullet.mp3')
#                     shot_sound.play()

#         if event.type == pygame.KEYUP:
#             if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
#                 player_change_x = 0

#     # Continuous shooting
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_SPACE] and not bullet_active:
#         bullet_x = player_x + 16
#         fire_bullet(bullet_x, bullet_y)
#         shot_sound = mixer.Sound('bullet.mp3')
#         shot_sound.play()

#     # Player movement logic
#     player_x += player_change_x
#     player_x = max(0, min(player_x, win_width - 64))

#     # Enemy movement
#     for i in range(enemy_count):
#         # Game over condition
#         if enemy_y[i] > 450:
#             for j in range(enemy_count):
#                 enemy_y[j] = 2000
#             display_game_over()
#             break

#         enemy_x[i] += enemy_change_x[i]
#         if enemy_x[i] <= 0 or enemy_x[i] >= win_width - 64:
#             enemy_change_x[i] *= -1
#             enemy_y[i] += enemy_change_y[i]

#         # Collision check
#         if check_collision(bullet_x, enemy_x[i], bullet_y, enemy_y[i]):
#             current_score += 1
#             bullet_y = player_y
#             bullet_active = False
#             enemy_x[i] = random.randint(50, 750)
#             enemy_y[i] = random.randint(30, 150)

#         draw_enemy(enemy_x[i], enemy_y[i], i)

#     # Bullet movement
#     if bullet_active:
#         fire_bullet(bullet_x, bullet_y)
#         bullet_y -= bullet_change_y
#         if bullet_y <= 0:
#             bullet_y = player_y
#             bullet_active = False

#     # Render player
#     draw_player(player_x, player_y)

#     # Display score
#     display_score(score_pos_x, score_pos_y)

#     # Update the display
#     pygame.display.update()

# pygame.quit()


import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Screen setup
win_width = 800
win_height = 600
window = pygame.display.set_mode((win_width, win_height))

# Title and icon
pygame.display.set_caption("Alien Blaster")

# Score settings
current_score = 0
score_pos_x = 10
score_pos_y = 10
score_font = pygame.font.Font('freesansbold.ttf', 20)

# Game Over text
end_game_font = pygame.font.Font('freesansbold.ttf', 64)

def display_score(x, y):
    score_text = score_font.render("Score: " + str(current_score), True, (255, 255, 255))
    window.blit(score_text, (x, y))

def display_game_over():
    over_text = end_game_font.render("GAME OVER", True, (255, 255, 255))
    window.blit(over_text, (200, 250))

# Background music
mixer.music.load('background.mp3')
mixer.music.play(-1)

# Player setup
player_img = pygame.image.load('me.jpeg')
player_img = pygame.transform.scale(player_img, (64, 64))
player_x = 370
player_y = 525
player_change_x = 0

# Enemy setup
enemy_images = []
enemy_x = []
enemy_y = []
enemy_change_x = []
enemy_change_y = []
enemy_count = 8



for _ in range(enemy_count):
    enemy_images.append(pygame.image.load('alien.png'))
    enemy_images[-1] = pygame.transform.scale(enemy_images[-1], (64, 64))
    enemy_x.append(random.randint(50, 750))
    enemy_y.append(random.randint(30, 150))
    enemy_change_x.append(1)
    enemy_change_y.append(40)

# Bullet setup
bullet_img = pygame.image.load('bullet.png')
bullet_img = pygame.transform.scale(bullet_img, (32, 64))
bullet_x = 0
bullet_y = player_y
bullet_change_y = 4
bullet_active = False

# Collision detection
def check_collision(obj1_x, obj2_x, obj1_y, obj2_y):
    distance = math.sqrt((math.pow(obj1_x - obj2_x, 2)) + (math.pow(obj1_y - obj2_y, 2)))
    return distance <= 50

# Player movement
def draw_player(x, y):
    window.blit(player_img, (x, y))

# Enemy rendering
def draw_enemy(x, y, idx):
    window.blit(enemy_images[idx], (x, y))

# Bullet movement
def fire_bullet(x, y):
    global bullet_active
    bullet_active = True
    window.blit(bullet_img, (x, y))

# Game loop
run_game = True
while run_game:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

        # Player control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -1.7
            if event.key == pygame.K_RIGHT:
                player_change_x = 1.7
            if event.key == pygame.K_SPACE and not bullet_active:
                bullet_x = player_x + 16
                fire_bullet(bullet_x, bullet_y)
                shot_sound = mixer.Sound('bullet.mp3')
                shot_sound.play()

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_change_x = 0

    # Continuous shooting
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not bullet_active:
        bullet_x = player_x + 16
        fire_bullet(bullet_x, bullet_y)
        shot_sound = mixer.Sound('bullet.mp3')
        shot_sound.play()

    # Player movement logic
    player_x += player_change_x
    player_x = max(0, min(player_x, win_width - 64))

    # Enemy movement
    for i in range(enemy_count):
        # Game over condition
        if enemy_y[i] > win_height - 120:  # Adjusted for game layout
            for j in range(enemy_count):
                enemy_y[j] = 2000
            display_game_over()
            run_game = False  # Stop the game loop
            break

        enemy_x[i] += enemy_change_x[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= win_width - 64:
            enemy_change_x[i] *= -1
            enemy_y[i] += enemy_change_y[i]

        # Ensure enemy doesn't move too far down
        enemy_y[i] = min(enemy_y[i], win_height - 120)

        # Collision check
        if check_collision(bullet_x, enemy_x[i], bullet_y, enemy_y[i]):
            current_score += 1
            bullet_y = player_y
            bullet_active = False
            enemy_x[i] = random.randint(50, 750)
            enemy_y[i] = random.randint(30, 150)

        draw_enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_active:
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_change_y
        if bullet_y <= 0:
            bullet_y = player_y
            bullet_active = False

    # Render player
    draw_player(player_x, player_y)

    # Display score
    display_score(score_pos_x, score_pos_y)

    # Update the display
    pygame.display.update()

pygame.quit()

