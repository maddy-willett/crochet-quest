import pygame


WIDTH = 960
HEIGHT = 540
FPS = 60

SKY_BLUE = (176, 220, 245)
GREEN_GRASS = (119, 177, 108)
YARN_BROWN = (91, 57, 40)
SKIN_TONE = (224, 170, 130)
DRESS_PURPLE = (132, 92, 156)
SHOE_BROWN = (79, 52, 40)

PLAYER_SPEED = 5
player_x = 100
player_y = 393

def draw_hero(screen, x, y):
    # Legs
    pygame.draw.line(screen, SKIN_TONE, (x + 14, y + 52), (x + 12, y + 72), 7)
    pygame.draw.line(screen, SKIN_TONE, (x + 32, y + 52), (x + 34, y + 72), 7)

    # Shoes
    pygame.draw.ellipse(screen, SHOE_BROWN, (x + 3, y + 68, 18, 9))
    pygame.draw.ellipse(screen, SHOE_BROWN, (x + 27, y + 68, 18, 9))

    # Dress
    pygame.draw.polygon(
        screen,
        DRESS_PURPLE,
        [(x + 12, y + 29), (x + 34, y + 29),
         (x + 42, y + 59), (x + 5, y + 59)],
    )

    # Head
    pygame.draw.circle(screen, SKIN_TONE, (x + 23, y + 19), 16)

    # Curly hair
    curls = [
        (x + 9, y + 10),
        (x + 16, y + 3),
        (x + 25, y + 2),
        (x + 34, y + 7),
        (x + 38, y + 16),
        (x + 8, y + 20),
    ]

    for curl in curls:
        pygame.draw.circle(screen, YARN_BROWN, curl, 8)

    # Eyes
    pygame.draw.circle(screen, YARN_BROWN, (x + 18, y + 19), 2)
    pygame.draw.circle(screen, YARN_BROWN, (x + 29, y + 19), 2)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crochet Quest")

clock = pygame.time.Clock()
running = True

while running:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update the game
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= PLAYER_SPEED

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += PLAYER_SPEED

    # Keep the heroine inside the window.
    player_x = max(0, min(player_x, WIDTH - 46))

    # 3. Draw the game
    screen.fill(SKY_BLUE)

    pygame.draw.rect(screen, GREEN_GRASS, (0, 470, WIDTH, 70))
    draw_hero(screen, player_x, player_y)

    # 4. Show the completed frame
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()