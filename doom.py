import pygame, math, sys, random
pygame.init()

# ---------- Screen & Raycasting settings ----------
WIDTH, HEIGHT = 1024, 640
HALF_HEIGHT = HEIGHT // 2
FOV = math.pi / 3  # 60 degrees
HALF_FOV = FOV / 2
NUM_RAYS = 160
MAX_DEPTH = 1000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * 40
SCALE = WIDTH // NUM_RAYS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 18)

# ---------- Map ----------
game_map = [
    "1111111111111111",
    "1..............1",
    "1..111....111..11",
    "1..............1",
    "1..11......11..1",
    "1......11......1",
    "1......11......1",
    "1..............1",
    "1111111111111111"
]
TILE = 100
MAP_W, MAP_H = len(game_map[0]), len(game_map)

# ---------- Player ----------
player_x, player_y = 160, 160
player_angle = 0
player_speed = 3.0
rot_speed = 0.05
player_health = 100
PLAYER_RADIUS = 15  # for collisions

# ---------- Enemies ----------
# Each enemy: dict with x,y,health,speed,alive
enemies = []
def spawn_enemy(x, y):
    enemies.append({
        "x": x, "y": y,
        "health": 3,
        "speed": 1.2,
        "alive": True,
        "last_damage_time": 0.0
    })

# Spawn a few enemies in open spaces
open_positions = []
for gy in range(MAP_H):
    for gx in range(MAP_W):
        if game_map[gy][gx] == ".":
            open_positions.append((gx * TILE + TILE//2, gy * TILE + TILE//2))
random.shuffle(open_positions)
for pos in open_positions[:6]:
    spawn_enemy(pos[0], pos[1])

# ---------- Bullets ----------
bullets = []  # each bullet: {"x","y","dx","dy","speed","life"}

BULLET_SPEED = 12
BULLET_LIFE = 60  # frames

# ---------- Helpers ----------
def is_wall(x, y):
    if x < 0 or y < 0: return True
    gx, gy = int(x // TILE), int(y // TILE)
    if gx < 0 or gy < 0 or gy >= MAP_H or gx >= MAP_W:
        return True
    return game_map[gy][gx] == "1"

def line_of_sight(x1, y1, x2, y2, step=5):
    # Walk from (x1,y1) toward (x2,y2) and see if any wall blocks view
    dx = x2 - x1
    dy = y2 - y1
    dist = math.hypot(dx, dy)
    if dist < 1: return True
    steps = int(dist / step)
    for i in range(1, steps+1):
        t = i / steps
        ix = x1 + dx * t
        iy = y1 + dy * t
        if is_wall(ix, iy):
            return False
    return True

def clamp(v, a, b):
    return max(a, min(b, v))

# ---------- Raycasting & Rendering ----------
def ray_casting(sc, px, py, pa):
    cur_angle = pa - HALF_FOV
    zbuffer = [float('inf')] * NUM_RAYS  # distances per ray
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        for depth in range(1, MAX_DEPTH):
            target_x = px + depth * cos_a
            target_y = py + depth * sin_a
            if is_wall(target_x, target_y):
                # Correct fish-eye
                depth_corrected = depth * math.cos(pa - cur_angle)
                proj_height = PROJ_COEFF / (depth_corrected + 0.0001)
                # shading by depth
                shade = 255 / (1 + depth_corrected * depth_corrected * 0.00001)
                color = (shade * 0.8, shade * 0.7, shade * 0.6)
                pygame.draw.rect(
                    sc, color,
                    (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height)
                )
                zbuffer[ray] = depth_corrected
                break

        cur_angle += DELTA_ANGLE

    # Render enemies as vertical sprites using zbuffer for occlusion
    for enemy in enemies:
        if not enemy["alive"]:
            continue
        # Compute vector from player to enemy
        dx = enemy["x"] - px
        dy = enemy["y"] - py
        dist = math.hypot(dx, dy)
        # angle from player's view
        ang = math.atan2(dy, dx)
        delta = ang - pa
        # Normalize delta angle to -PI..PI
        while delta > math.pi: delta -= 2 * math.pi
        while delta < -math.pi: delta += 2 * math.pi

        if -HALF_FOV - 0.2 < delta < HALF_FOV + 0.2 and dist > 10:
            # screen x position
            proj_x = (delta + HALF_FOV) / FOV * WIDTH
            # size scaled by distance
            depth_corrected = dist * math.cos(delta)
            sprite_height = PROJ_COEFF / (depth_corrected + 0.0001)
            sprite_width = sprite_height * 0.6
            top = HALF_HEIGHT - sprite_height // 2
            left = int(proj_x - sprite_width // 2)

            # occlusion test: check a few ray columns around this x if they are closer
            col = int(proj_x / SCALE)
            occluded = False
            if 0 <= col < NUM_RAYS:
                if zbuffer[col] < depth_corrected:
                    occluded = True

            if not occluded:
                # Draw a simple enemy sprite: a rounded rectangle with a "face"
                enemy_surf = pygame.Surface((int(sprite_width), int(sprite_height)), pygame.SRCALPHA)
                # body
                pygame.draw.ellipse(enemy_surf, (200, 40, 40), enemy_surf.get_rect())
                # eyes
                ew = enemy_surf.get_width()
                eh = enemy_surf.get_height()
                pygame.draw.circle(enemy_surf, (30, 30, 30), (int(ew*0.35), int(eh*0.35)), max(1, int(eh*0.06)))
                pygame.draw.circle(enemy_surf, (30, 30, 30), (int(ew*0.65), int(eh*0.35)), max(1, int(eh*0.06)))
                # health bar on top
                hb_w = int(ew * (enemy["health"] / 3))
                pygame.draw.rect(enemy_surf, (0, 0, 0), (0, 0, ew, int(eh*0.1)))
                pygame.draw.rect(enemy_surf, (0, 255, 0), (2, 2, max(0, hb_w-4), int(eh*0.06)))
                sc.blit(enemy_surf, (left, top))

    # Return zbuffer to let weapon/projectiles be drawn in front if needed
    return zbuffer

# ---------- UI: Minimap & Weapon & HUD ----------
MINIMAP_SCALE = 0.12
MINIMAP_TILE = int(TILE * MINIMAP_SCALE)
MINIMAP_POS = (10, 10)
def draw_minimap(sc, px, py, pa):
    mx, my = MINIMAP_POS
    # background
    map_w_px = MAP_W * MINIMAP_TILE
    map_h_px = MAP_H * MINIMAP_TILE
    pygame.draw.rect(sc, (20, 20, 20), (mx-2, my-2, map_w_px+4, map_h_px+4))
    # draw map tiles
    for y in range(MAP_H):
        for x in range(MAP_W):
            rect = (mx + x * MINIMAP_TILE, my + y * MINIMAP_TILE, MINIMAP_TILE, MINIMAP_TILE)
            if game_map[y][x] == "1":
                pygame.draw.rect(sc, (200, 200, 200), rect)
            else:
                pygame.draw.rect(sc, (30, 30, 30), rect)

    # draw enemies
    for e in enemies:
        if not e["alive"]: continue
        ex = mx + (e["x"] / TILE) * MINIMAP_TILE
        ey = my + (e["y"] / TILE) * MINIMAP_TILE
        pygame.draw.circle(sc, (200, 30, 30), (int(ex), int(ey)), max(2, MINIMAP_TILE//4))

    # draw player
    px_m = mx + (px / TILE) * MINIMAP_TILE
    py_m = my + (py / TILE) * MINIMAP_TILE
    pygame.draw.circle(sc, (50, 200, 50), (int(px_m), int(py_m)), max(3, MINIMAP_TILE//3))
    # direction line
    dx = math.cos(pa) * 20
    dy = math.sin(pa) * 20
    pygame.draw.line(sc, (200, 200, 50), (px_m, py_m), (px_m + dx, py_m + dy), 2)

def draw_weapon(sc, fire_recoil):
    # Stylized weapon at bottom-center
    w = WIDTH
    h = HEIGHT
    base_y = h - 30
    center_x = w // 2
    # recoil shifts the weapon a bit
    rx = center_x + int(math.sin(fire_recoil * 3.0) * 4)
    ry = base_y - int(fire_recoil * 10)

    # layered shapes to make it look like a stylized Doom pistol
    # shadow
    pygame.draw.polygon(sc, (10,10,10), [
        (rx - 140, ry + 30),
        (rx + 140, ry + 30),
        (rx + 90, ry + 60),
        (rx - 90, ry + 60)
    ])
    # body
    pygame.draw.rect(sc, (60, 60, 70), (rx - 120, ry, 240, 40), border_radius=8)
    # barrel
    pygame.draw.rect(sc, (80,80,100), (rx + 40, ry - 18, 70, 20), border_radius=4)
    # grip
    pygame.draw.polygon(sc, (50,50,60), [
        (rx - 120, ry + 40),
        (rx - 80, ry + 40),
        (rx - 40, ry + 80),
        (rx - 120, ry + 80)
    ])
    # metal highlights
    pygame.draw.rect(sc, (120,120,140), (rx - 60, ry + 6, 80, 6), border_radius=3)
    # muzzle flash if firing (small triangle)
    if fire_recoil > 0.1:
        pygame.draw.polygon(sc, (255, 200, 80), [
            (rx + 110, ry - 2 + random.randint(-2,2)),
            (rx + 140, ry + 10 + random.randint(-2,2)),
            (rx + 110, ry + 22 + random.randint(-2,2))
        ])

def draw_hud(sc, health):
    # Health bar
    bar_w = 200
    bar_h = 20
    x = 20
    y = HEIGHT - 40
    pygame.draw.rect(sc, (30,30,30), (x-2, y-2, bar_w+4, bar_h+4))
    pygame.draw.rect(sc, (80, 0, 0), (x, y, bar_w, bar_h))
    pygame.draw.rect(sc, (0, 220, 0), (x, y, int(bar_w * (health / 100)), bar_h))
    text = FONT.render(f"HEALTH: {int(health)}", True, (255,255,255))
    sc.blit(text, (x + bar_w + 10, y))

# ---------- Movement & Game Logic ----------
def move_player(keys):
    global player_x, player_y, player_angle
    if keys[pygame.K_a]:
        player_angle -= rot_speed
    if keys[pygame.K_d]:
        player_angle += rot_speed

    # forward/back movement with collision (use small step checking)
    move_dx = math.cos(player_angle) * player_speed
    move_dy = math.sin(player_angle) * player_speed

    if keys[pygame.K_w]:
        nx = player_x + move_dx
        ny = player_y + move_dy
        # circle collision sampling: check several offsets for smooth sliding
        if not is_wall(nx + PLAYER_RADIUS * 0.5, ny) and not is_wall(nx - PLAYER_RADIUS * 0.5, ny) and not is_wall(nx, ny + PLAYER_RADIUS * 0.5):
            player_x, player_y = nx, ny
    if keys[pygame.K_s]:
        nx = player_x - move_dx
        ny = player_y - move_dy
        if not is_wall(nx + PLAYER_RADIUS * 0.5, ny) and not is_wall(nx - PLAYER_RADIUS * 0.5, ny) and not is_wall(nx, ny - PLAYER_RADIUS * 0.5):
            player_x, player_y = nx, ny

def update_enemies(dt):
    global player_x, player_y, player_health
    now = pygame.time.get_ticks() / 1000.0
    for e in enemies:
        if not e["alive"]:
            continue
        ex, ey = e["x"], e["y"]
        dx = player_x - ex
        dy = player_y - ey
        dist = math.hypot(dx, dy)

        # If player in sight and within chase range, move toward player
        CHASE_RANGE = 700
        if dist < CHASE_RANGE and line_of_sight(ex, ey, player_x, player_y):
            # Move toward player with collision checks (small steps)
            dirx = dx / (dist + 0.0001)
            diry = dy / (dist + 0.0001)
            step = e["speed"]
            # attempt move on x
            new_x = ex + dirx * step
            if not is_wall(new_x, ey):
                e["x"] = new_x
            # attempt move on y
            new_y = ey + diry * step
            if not is_wall(e["x"], new_y):
                e["y"] = new_y

        # If enemy touches player, damage
        TOUCH_RADIUS = 28
        if dist < TOUCH_RADIUS:
            # damage every 0.5 seconds on touch
            if now - e["last_damage_time"] > 0.5:
                player_health -= 10
                e["last_damage_time"] = now
                # small pushback for player
                knock_x = -dirx * 8
                knock_y = -diry * 8
                # attempt to move player back slightly if not blocked
                if not is_wall(player_x + knock_x, player_y + knock_y):
                    player_x += knock_x
                    player_y += knock_y

def update_bullets():
    # Move bullets; remove on wall hit or life expired; handle hit vs enemies
    to_remove = []
    for i, b in enumerate(bullets):
        b["x"] += b["dx"] * b["speed"]
        b["y"] += b["dy"] * b["speed"]
        b["life"] -= 1
        if is_wall(b["x"], b["y"]) or b["life"] <= 0:
            to_remove.append(i)
            continue
        # collision vs enemies
        for e in enemies:
            if not e["alive"]: continue
            dist = math.hypot(e["x"] - b["x"], e["y"] - b["y"])
            if dist < 25:
                e["health"] -= 1
                to_remove.append(i)
                if e["health"] <= 0:
                    e["alive"] = False
                break
    # remove bullets by indices in reverse
    for i in sorted(to_remove, reverse=True):
        bullets.pop(i)

# ---------- Main loop ----------
fire_cooldown = 0.12  # seconds between shots
last_fire_time = 0
fire_recoil = 0.0

while True:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    keys = pygame.key.get_pressed()

    # Shooting
    if keys[pygame.K_SPACE]:
        t = pygame.time.get_ticks() / 1000.0
        if t - last_fire_time >= fire_cooldown:
            # spawn bullet from player position with slight forward offset
            bx = player_x + math.cos(player_angle) * 20
            by = player_y + math.sin(player_angle) * 20
            bullets.append({
                "x": bx, "y": by,
                "dx": math.cos(player_angle), "dy": math.sin(player_angle),
                "speed": BULLET_SPEED, "life": BULLET_LIFE
            })
            last_fire_time = t
            fire_recoil = 1.0  # used by weapon drawing

    # update recoil decay
    fire_recoil = max(0.0, fire_recoil - dt * 6.0)

    move_player(keys)
    update_enemies(dt)
    update_bullets()

    # Rendering
    screen.fill((20, 20, 30))  # sky-ground are combined simply
    zbuffer = ray_casting(screen, player_x, player_y, player_angle)

    # Draw bullets as small bright dots projected in front (2D or attempt to put them in 3D)
    # For simplicity, draw them as HUD-level flashes (appear in world but not using zbuffer occlusion).
    for b in bullets:
        # compute distance from player and if in view then draw as small rectangle in 3D-ish
        bx, by = b["x"], b["y"]
        dx = bx - player_x
        dy = by - player_y
        dist = math.hypot(dx, dy)
        ang = math.atan2(dy, dx)
        delta = ang - player_angle
        while delta > math.pi: delta -= 2 * math.pi
        while delta < -math.pi: delta += 2 * math.pi
        if -HALF_FOV < delta < HALF_FOV:
            proj_x = (delta + HALF_FOV) / FOV * WIDTH
            depth_corr = dist * math.cos(delta)
            size = PROJ_COEFF / (depth_corr + 0.0001) * 0.03
            pygame.draw.circle(screen, (255, 220, 100), (int(proj_x), int(HALF_HEIGHT)), max(1, int(size)))

    # Draw minimap
    draw_minimap(screen, player_x, player_y, player_angle)

    # Draw bullets on minimap (small points)
    mx, my = MINIMAP_POS
    for b in bullets:
        bx = mx + (b["x"] / TILE) * MINIMAP_TILE
        by = my + (b["y"] / TILE) * MINIMAP_TILE
        pygame.draw.circle(screen, (255, 200, 80), (int(bx), int(by)), 2)

    # Draw HUDs
    draw_hud(screen, clamp(player_health, 0, 100))
    draw_weapon(screen, fire_recoil)

    # Game over check
    if player_health <= 0:
        # render "Game Over" overlay
        go_text = FONT.render("GAME OVER - press R to respawn", True, (255,255,255))
        screen.blit(go_text, (WIDTH//2 - go_text.get_width()//2, HEIGHT//2))
        # allow respawn
        if keys[pygame.K_r]:
            # respawn player and reset enemies
            player_health = 100
            player_x, player_y = 160, 160
            enemies.clear()
            for pos in open_positions[:6]:
                spawn_enemy(pos[0], pos[1])
            bullets.clear()

    pygame.display.flip()