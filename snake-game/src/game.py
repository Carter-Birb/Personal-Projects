import pygame
from time import time
from random import randint
from grid import Grid
from fruit import Fruit
from snake import Snake

class SnakeGame:
    
    # Game constants
    WIDTH, HEIGHT = 600, 600
    MAXFPS = 60
    GRIDSIZE = 20
    DEBUG = True
    
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Setup the display
        self.screen = pygame.display.set_mode((SnakeGame.WIDTH, SnakeGame.HEIGHT))
        pygame.display.set_caption("Silly Snake Game")
        
        # Setup the grid
        self.grid = Grid(600, 600, SnakeGame.GRIDSIZE)
        
        # Setup the snake
        self.snake = Snake((self.grid.columns // 2, self.grid.rows // 2), "RIGHT", (0, 255, 0), SnakeGame.GRIDSIZE)
        self.snake_speed = 10 # grids per second
        # Begin time to move the snake based on self.snakespeed
        self.last_snake_move = time()
        self.snake_alive = True
        
        # Setup first fruit
        self.fruit_x = randint(1, self.grid.columns - 2)
        self.fruit_y = randint(1, self.grid.rows - 2)
        self.fruit = Fruit((self.fruit_x, self.fruit_y), (255, 0, 0), SnakeGame.GRIDSIZE)
        self.grid.place_fruit((self.fruit_x, self.fruit_y), SnakeGame.DEBUG)
        
        # Setup font
        self.font = pygame.font.SysFont("couriernew", 20)
        
        # Setup clock
        self.clock = pygame.time.Clock()
        
        # Setup game variables
        self.running = True
        
        # Contain the player's score
        self.score = 0
    
    
    def run(self):
        '''
        contains the game loop
        '''
        while self.running:
            
            # Handle events
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.running = False
        
            keys = pygame.key.get_pressed()
        
            if self.snake_alive:
                # Controls the direction of the snake/prevents the snake from moving the opposite direction
                if keys[pygame.K_w] and self.snake.direction != "DOWN":
                    self.snake.direction = "UP"
                elif keys[pygame.K_a] and self.snake.direction != "RIGHT":
                    self.snake.direction = "LEFT"
                elif keys[pygame.K_s] and self.snake.direction != "UP":
                    self.snake.direction = "DOWN"
                elif keys[pygame.K_d] and self.snake.direction != "LEFT":
                    self.snake.direction = "RIGHT"
            
            # Update game state
            self.update()
            
            # Render game
            self.render()
            
            # Cap the FPS to 60
            self.clock.tick(SnakeGame.MAXFPS)
        
        pygame.quit()
    
    
    def update(self):
        '''
        updates the gamestate (e.g., move snake, check for collisions, update score)
        '''
        # Sets the current snake move time
        if self.snake_alive:
            current_snake_move = time()
            if current_snake_move - self.last_snake_move >= 1 / self.snake_speed:
                # Moves the snake depending on the snake speed
                self.snake.move()
                self.last_snake_move = current_snake_move
            
            head_x, head_y = self.snake.body[0]
            
            # Checks for collisions with the border
            border_touched = self.grid.check_border_collision(SnakeGame.DEBUG)
            
            # Checks for collisions with the snake
            snake_touched = self.snake.check_collision(SnakeGame.DEBUG)
            
            # Checks for collisions with fruit
            fruit_collected = self.grid.check_fruit_collision(head_x, head_y, self.fruit_x, self.fruit_y, SnakeGame.DEBUG)

            # Updates the snake's position within the grid list
            self.grid.update_snake(self.snake.body, SnakeGame.DEBUG)
            
            # Handles the various events when a fruit is obtained by the snake
            if fruit_collected:
                # Generates a new fruit
                self.fruit_x = randint(1, self.grid.columns - 2)
                self.fruit_y = randint(1, self.grid.rows - 2)
                self.fruit = Fruit((self.fruit_x, self.fruit_y), (255, 0, 0), SnakeGame.GRIDSIZE)
                self.grid.place_fruit((self.fruit_x, self.fruit_y), SnakeGame.DEBUG)
                
                # Increased the player's score
                self.score += 1
                
                # Increases the size of the snake
                self.snake.grow()
            
            # Handles when the snake touches a border OR itself
            if border_touched or snake_touched:
                self.running = False
    
    
    def render(self):
        '''
        renders the game (e.g., draw snake, draw food, draw borders, place text)
        '''
        self.screen.fill((0, 0, 0))
        
        # Border attributes
        border_thickness = 20
        border_color = (128, 128, 128)
        
        # Renders the borders of the game
        for i in range(4):
            if i == 0:  # Top border
                pygame.draw.rect(self.screen, border_color, pygame.Rect(0, 0, SnakeGame.WIDTH, border_thickness))
            elif i == 1:  # Left border
                pygame.draw.rect(self.screen, border_color, pygame.Rect(0, 0, border_thickness, SnakeGame.HEIGHT))
            elif i == 2:  # Bottom border
                pygame.draw.rect(self.screen, border_color, pygame.Rect(0, SnakeGame.HEIGHT - border_thickness, SnakeGame.WIDTH, border_thickness))
            elif i == 3:  # Right border
                pygame.draw.rect(self.screen, border_color, pygame.Rect(SnakeGame.WIDTH - border_thickness, 0, border_thickness, SnakeGame.HEIGHT))
        
        # Renders the score text
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (0, 0))
        
        # Renders the snake
        self.snake.draw_snake(self.screen)
        
        # Renders the fruit
        self.fruit.draw_fruit(self.screen)
        
        # Renders the grid if debugging is True, renders the background otherwise
        self.grid.draw_grid(self.screen, SnakeGame.DEBUG)
        
        pygame.display.flip()

S = SnakeGame()
S.run()