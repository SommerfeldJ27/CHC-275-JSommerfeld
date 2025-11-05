import pygame
import math
import sys

# Screen settings
WIDTH, HEIGHT = 800, 600
HALF_HEIGHT = HEIGHT // 2
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * 40
SCALE = WIDTH // NUM_RAYS

# Map (1 = wall, 0 = empty space)
game_map = [
    "111111111111",
    "1..........1",
    "1..........1",
    "1....11....1",
    "1..........1",
    "1..........1",
    "111111111111"
]
TILE = 100

# Player
player_x, player_y = 150, 150
player_angle = 0
player_speed = 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE

def ray_casting(sc, px, py, pa):
    cur_angle = pa - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        for depth in range(MAX_DEPTH):
            target_x = px + depth * cos_a
            target_y = py + depth * sin_a
            if game_map[int(target_y // TILE)][int(target_x // TILE)] == '1':
                depth *= math.cos(pa - cur_angle)  # fix fish-eye
                proj_height = PROJ_COEFF / (depth + 0.0001)
                color = (200 / (1 + depth * depth * 0.0001),) * 3
                pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_x += player_speed * math.cos(player_angle)
        player_y += player_speed * math.sin(player_angle)
    if keys[pygame.K_s]:
        player_x -= player_speed * math.cos(player_angle)
        player_y -= player_speed * math.sin(player_angle)
    if keys[pygame.K_a]:
        player_angle -= 0.05
    if keys[pygame.K_d]:
        player_angle += 0.05

    screen.fill((0, 0, 0))
    ray_casting(screen, player_x, player_y, player_angle)
    pygame.display.flip()
    clock.tick(60)
