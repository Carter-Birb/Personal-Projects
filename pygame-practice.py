import pygame
from math import sqrt
from random import randint
import time

# Initialize Pygame
pygame.init()

# Debugging
DEBUG = True
last_debug_time = time.time()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")
clock = pygame.time.Clock()

# Render font
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 30)

# Sound effects
coin_sound = pygame.mixer.Sound("Sound Effects/coin-collect-retro-8-bit-sound-effect-145251.mp3")
death_sound = pygame.mixer.Sound("Sound Effects\glitch-scream-305035.mp3")
music = pygame.mixer.Sound("Sound Effects\8-bit-loop-189494.mp3")

# Sound effects volume
coin_sound.set_volume(0.5)
death_sound.set_volume(0.1)
music.set_volume(0.1)

# Begins the background music to play indefinitely
music.play(-1)

# Player properties
player_x, player_y = 700, 300
player_radius = 10
player_speed_x = 5
player_speed_y = 5
coins_collected = 0
player_alive = True

# Enemy properties
enemy_width = 10
enemy_height = 10
enemy_speed = 10
enemy_x, enemy_y = WIDTH // 2, enemy_height
enemy_direction = 1  # 1 for down, -1 for up

# Coin properties
coin_radius = 8
num_coins = 20

# Generate coin locations
coins = []
for _ in range(num_coins):
    coin_x = randint(coin_radius, WIDTH - coin_radius)
    coin_y = randint(coin_radius, HEIGHT - coin_radius)
    coins.append({'x': coin_x, 'y': coin_y, 'radius': coin_radius, 'collected': False})

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fills the screen with black
    
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Allows the window to be closed
            running = False
    
    keys = pygame.key.get_pressed()
    
    if player_alive:
        # Controls the movement of the player
        if keys[pygame.K_w]:
            player_y -= player_speed_y
        if keys[pygame.K_a]:
            player_x -= player_speed_x
        if keys[pygame.K_s]:
            player_y += player_speed_y
        if keys[pygame.K_d]:
            player_x += player_speed_x
    
        player_x = max(player_radius, min(player_x, WIDTH - player_radius))
        player_y = max(player_radius, min(player_y, HEIGHT - player_radius))
    
        # Draws the player
        pygame.draw.circle(screen, (225, 0, 0), (player_x, player_y), player_radius)
    
        # Detects the player's collision with a coin
        for coin in coins:
            if not coin['collected']:
                coin_distance = sqrt(((player_x - coin['x']) ** 2) + ((player_y - coin['y']) ** 2))
                if coin_distance <= (player_radius + coin['radius']):
                    coin['collected'] = True
                    coin_sound.play()
                    coins_collected += 1
                    if DEBUG:
                        print("The player collided with a coin")
                    
    
        # Detects the player's collision with an enemy
        enemy_distance = sqrt(((player_x - enemy_x) ** 2) + ((player_y - enemy_y) ** 2))
        if enemy_distance <= (player_radius + enemy_width):
            player_alive = False
            music.stop() # Stops the background music
            death_sound.play()
            if DEBUG:
                print("The player collided with an enemy")
    
    # Draws the game objects
    for coin in coins:
        if not coin['collected']:
            pygame.draw.circle(screen, (255, 255, 0), (coin['x'], coin['y']), coin['radius'])
    
    pygame.draw.rect(screen, (0, 0, 255), (enemy_x, enemy_y, enemy_width, enemy_height))
    
    # Controls the movement of the enemy square
    enemy_y += enemy_speed * enemy_direction
    if enemy_y <= enemy_height or enemy_y >= HEIGHT - enemy_height:
        enemy_direction *= -1  # Reverses the direction of the enemy
    
    # Render text
    if coins_collected == num_coins:
        text_surface = font.render(f"You Win!", True, (255, 255, 255))
        screen.blit(text_surface, (0, 0))
    elif not player_alive:
        text_surface = font.render(f"You died.", True, (255, 255, 255))
        screen.blit(text_surface, (0, 0))
    else:
        text_surface = font.render(f"Coins Collected: {coins_collected}", True, (225, 255, 255))
        screen.blit(text_surface, (0, 0))
    
    pygame.display.flip()  # Updates the display
    
    # Print debug info every 0.2 seconds
    current_time = time.time()
    if DEBUG and current_time - last_debug_time >= 0.2:
        print(f"Player x: {player_x} Player y: {player_y} Enemy x: {enemy_x} Enemy y: {enemy_y}")
        last_debug_time = current_time

    clock.tick(60) # Limits the fps to 60

pygame.quit()