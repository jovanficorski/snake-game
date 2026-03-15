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

WIN_SCORE = 7

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


def create_walls(level):
    walls = []

    # Level 2 -> надворешни ѕидови
    if level >= 2:
        for x in range(0, WIDTH, CELL_SIZE):
            walls.append((x, 0))
            walls.append((x, HEIGHT - CELL_SIZE))

        for y in range(0, HEIGHT, CELL_SIZE):
            walls.append((0, y))
            walls.append((WIDTH - CELL_SIZE, y))

    # Level 3 -> неколку пречки во полето
    if level == 3:

        obstacles = [
            (200, 200), (220, 200), (240, 200),
            (360, 300), (380, 300), (400, 300),
            (160, 420), (160, 440), (160, 460),
            (420, 120), (440, 120), (460, 120)
        ]

        walls.extend(obstacles)

    return walls


walls = create_walls(level)


def generate_food():
    while True:
        pos = (
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)
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
    rect = text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(text, rect)


def show_message(message):
    font = pygame.font.SysFont(None, 60)
    text = font.render(message, True, WHITE)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)


def countdown():
    font = pygame.font.SysFont(None, 100)

    for i in ["3", "2", "1"]:
        screen.fill(BLACK)
        text = font.render(i, True, WHITE)
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, rect)
        pygame.display.flip()
        pygame.time.delay(1000)


def draw_restart_button():
    font = pygame.font.SysFont(None, 40)
    rect = pygame.Rect(WIDTH // 2 - 80, HEIGHT // 2 + 60, 160, 50)

    pygame.draw.rect(screen, WHITE, rect)

    text = font.render("RESTART", True, BLACK)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

    return rect


countdown()

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

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if restart_rect.collidepoint(event.pos):
                level = 1
                score = 0
                snake = reset_snake()
                direction = (CELL_SIZE, 0)
                walls = create_walls(level)
                food = generate_food()
                game_over = False
                countdown()

    if not game_over:

        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]

        # teleport само за level 1
        if level == 1:

            if head_x < 0:
                head_x = WIDTH - CELL_SIZE
            elif head_x >= WIDTH:
                head_x = 0

            if head_y < 0:
                head_y = HEIGHT - CELL_SIZE
            elif head_y >= HEIGHT:
                head_y = 0

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
                        countdown()

                    else:
                        game_over = True
                        game_result = "YOU WIN!"

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
        restart_rect = draw_restart_button()

    pygame.display.flip()