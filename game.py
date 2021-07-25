import pygame
from sys import exit
from random import randint


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(books_surface, obstacle_rect)
            else:
                screen.blit(wall_surface, obstacle_rect)

        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Don\'t Touch My Stuff!')
clock = pygame.time.Clock()
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)
test2_font = pygame.font.Font('./font/Pixeltype.ttf', 100)
game_active = True

room_surface = pygame.image.load('./graphics/room.png').convert_alpha()
ground_surface = pygame.image.load('./graphics/ground-1.png').convert_alpha()
text_surface = test_font.render('Don\'t Touch My Stuff!', False, 'Black')
gameover_surface = test2_font.render('GAME OVER', False, 'Black')
gameover2_surface = test_font.render('Press SPACE button', False, 'Black')
oldersis_surface = pygame.image.load(
    './graphics/older_sister.png').convert_alpha()

# Obstacles
books_surface = pygame.image.load(
    './graphics/books.png').convert_alpha()

wall_surface = pygame.image.load('./graphics/wall.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load(
    './graphics/sister.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

        if event.type == obstacle_timer:
            if randint(0, 2):
                obstacle_rect_list.append(books_surface.get_rect(
                    bottomright=(randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(wall_surface.get_rect(
                    bottomright=(randint(900, 1100), 200)))

    if game_active:
        # Background
        screen.blit(room_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (40, 10))

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill('Grey')
        screen.blit(gameover_surface, (250, 150))
        screen.blit(gameover2_surface, (255, 250))
        screen.blit(oldersis_surface, (370, 290))
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

    pygame.display.update()
    clock.tick(60)
