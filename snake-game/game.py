import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")
clock = pygame.time.Clock()

# Player properties
player_x, player_y = 400, 300
player_radius = 10
player_speed_x = 5
player_speed_y = 5

# Coin locations
coins = [
    {"x": 750, "y": 550, "radius": 8, "collected": False},
    {"x": 750, "y": 50, "radius": 8, "collected": False},
    {"x": 50, "y": 550, "radius": 8, "collected": False},
    {"x": 50, "y": 50, "radius": 8, "collected": False}
]

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fills the screen with black
    
    
    # Draws the game objects
    for coin in coins:
        if not coin['collected']:
            pygame.draw.circle(screen, (255, 255, 0), (coin['x'], coin['y']), coin['radius'])
        
    pygame.draw.circle(screen, (225, 0, 0), (player_x, player_y), player_radius)
    
    
    # Controls the Movement of the RED circle aswell as events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Allows the window to be closed
            running = False
    
    keys = pygame.key.get_pressed()
    
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
    
    
    # Detects the player's collision with a coin
    for coin in coins:
        if not coin['collected']:
            distance = math.sqrt(((player_x - coin['x']) ** 2) + ((player_y - coin['y']) ** 2))
            if distance <= (player_radius + coin['radius']):
                coin['collected'] = True
                print("The player collected a coin!")
    
    
    pygame.display.flip()  # Updates the display

    clock.tick(60)

pygame.quit()