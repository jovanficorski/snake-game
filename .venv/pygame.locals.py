import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (140, 140, 140)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - 3 Levels")

clock = pygame.time.Clock()

WIN_SCORE = 25

level = 1
score = 0
game_over = False
game_result = ""

center_x = (WIDTH // 2) // CELL_SIZE * CELL_SIZE
center_y = (HEIGHT // 2) // CELL_SIZE * CELL_SIZE


def reset_snake():
    return [(center_x, center_y)]


snake = reset_snake()
direction = (CELL_SIZE, 0)



# kreirame dzidovi po nivo.


def create_walls(level):
    walls = []

    # ova e ramka kade da se nadvoresnite dzidovi
    for x in range(0, WIDTH, CELL_SIZE):
        walls.append((x, 0))
        walls.append((x, HEIGHT - CELL_SIZE))

    for y in range(0, HEIGHT, CELL_SIZE):
        walls.append((0, y))
        walls.append((WIDTH - CELL_SIZE, y))

    if level == 2:
        # kade da dodademe dzidovi vo level 2
        for x in range(100, 300, CELL_SIZE):
            walls.append((x, 150))

        for y in range(300, 500, CELL_SIZE):
            walls.append((400, y))

    if level == 3:
        # kade da dodademe dzidovi za level 3
        for x in range(80, 520, CELL_SIZE):
            if x < center_x - 60 or x > center_x + 60:
                walls.append((x, 200))
                walls.append((x, 400))

        for y in range(100, 500, CELL_SIZE):
            if y < center_y - 60 or y > center_y + 60:
                walls.append((150, y))
                walls.append((450, y))

    return walls


walls = create_walls(level)

# kako da se pojavuva hranata random.
def generate_food():
    while True:
        pos = (
            random.randrange(CELL_SIZE, WIDTH - CELL_SIZE, CELL_SIZE),
            random.randrange(CELL_SIZE, HEIGHT - CELL_SIZE, CELL_SIZE)
        )
        if pos not in snake and pos not in walls:
            return pos


food = generate_food()


def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))


def draw_food():
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))


def draw_walls():
    for wall in walls:
        pygame.draw.rect(screen, GRAY, (*wall, CELL_SIZE, CELL_SIZE))


def show_score():
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Level: {level}  Score: {score}", True, WHITE)
    screen.blit(text, (350, 10))


def show_message(message):
    font = pygame.font.SysFont(None, 60)
    text = font.render(message, True, WHITE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)


# ======================
# tuka e glavnata logika na igrata.
# ======================

while True:
    clock.tick(12)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    if not game_over:
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        new_head = (head_x, head_y)

        if new_head in walls or new_head in snake:
            game_over = True
            game_result = "YOU LOSE"

        else:
            snake.insert(0, new_head)

            if new_head == food:
                score += 1

                if score >= WIN_SCORE:
                    if level < 3:
                        level += 1
                        score = 0
                        snake = reset_snake()
                        direction = (CELL_SIZE, 0)
                        walls = create_walls(level)
                        food = generate_food()
                    else:
                        game_over = True
                        game_result = "YOU BEAT ALL LEVELS!"
                else:
                    food = generate_food()
            else:
                snake.pop()

    screen.fill(BLACK)
    draw_walls()
    draw_snake()
    draw_food()
    show_score()

    if game_over:
        show_message(game_result)

    pygame.display.flip()