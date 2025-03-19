import pygame
from time import time
from grid import Grid
from fruit import Fruit
from snake import Snake

class SnakeGame:
    
    # Game constants
    WIDTH, HEIGHT = 600, 600
    MAXFPS = 60
    GRIDSIZE = 50
    MOVE_COOLDOWN = 0.1 # Seconds 
    DEBUG = False
    
    def __init__(self):
        # Initialize pygame
        pygame.init()
        
        # Setup the display
        self.screen = pygame.display.set_mode((SnakeGame.WIDTH, SnakeGame.HEIGHT))
        pygame.display.set_caption("Silly Snake Game")
        
        # Setup sound effects
        self.fruit_sound = pygame.mixer.Sound("assets/sounds/one_beep-99630.mp3")
        self.fruit_sound.set_volume(0.5)
        
        # Setup the grid
        self.grid = Grid(SnakeGame.WIDTH, SnakeGame.HEIGHT, SnakeGame.GRIDSIZE)
        self.border_color = (100, 100, 100)
        
        # Setup the snake
        self.snake = Snake((self.grid.columns // 2, self.grid.rows // 2), "RIGHT", (0, 255, 0), SnakeGame.GRIDSIZE)
        self.snake_speed = 7 # grids per second
        # Begin time to move the snake based on self.snakespeed
        self.last_snake_move = time()
        self.snake_alive = True
        
        # Setup first fruit
        self.fruit = Fruit(self.grid.rows, self.grid.columns, self.snake.body, (255, 0, 0), SnakeGame.GRIDSIZE)
        self.fruit_x, self.fruit_y = self.fruit.position
        self.grid.place_fruit((self.fruit_x, self.fruit_y), SnakeGame.DEBUG)
        
        # Setup font
        self.font = pygame.font.SysFont("couriernew", 20)
        
        # Setup clock
        self.clock = pygame.time.Clock()
        
        # Setup game variables
        self.running = True
        
        # Contain the player's score
        self.score = 0
        
        # Contain the player's last movement time
        self.last_movement_time = 0
        
        # Render the game
        self.render()
    
    
    def run(self):
        '''
        contains the game loop
        '''
        while self.running:
            
                        
            # Update game state
            self.update()
            
            # Render game
            self.render()
            
            # Handle events
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.running = False
        
            keys = pygame.key.get_pressed()
        
            if self.snake_alive:
                # Implements the movement delay to prevent the user from making direction changes too quickly
                current_time = time()
                # Controls the direction of the snake/prevents the snake from moving the opposite direction
                if current_time - self.last_movement_time > SnakeGame.MOVE_COOLDOWN:  # Check for cooldown
                    if keys[pygame.K_w] and self.snake.direction != "DOWN":
                        self.snake.change_direction("UP")
                        self.last_movement_time = current_time  # Update the last direction change time
                    elif keys[pygame.K_a] and self.snake.direction != "RIGHT":
                        self.snake.change_direction("LEFT")
                        self.last_movement_time = current_time
                    elif keys[pygame.K_s] and self.snake.direction != "UP":
                        self.snake.change_direction("DOWN")
                        self.last_movement_time = current_time
                    elif keys[pygame.K_d] and self.snake.direction != "LEFT":
                        self.snake.change_direction("RIGHT")
                        self.last_movement_time = current_time
            
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
            border_touched = self.grid.check_border_collision(self.snake.body[0], SnakeGame.DEBUG)
            
            # Checks for collisions with the snake
            snake_touched = self.snake.check_collision(SnakeGame.DEBUG)
            
            # Checks for collisions with fruit
            fruit_collected = self.grid.check_fruit_collision(head_x, head_y, self.fruit_x, self.fruit_y, SnakeGame.DEBUG)

            # Updates the snake's position within the grid list
            self.grid.update_snake(self.snake.body, SnakeGame.DEBUG)
            
            # Handles the various events when a fruit is obtained by the snake
            if fruit_collected:
                # Generates a new fruit
                self.fruit = Fruit(self.grid.rows, self.grid.columns, self.snake.body, (255, 0, 0), SnakeGame.GRIDSIZE)
                self.fruit_x, self.fruit_y = self.fruit.position
                self.grid.place_fruit((self.fruit_x, self.fruit_y), SnakeGame.DEBUG)
                
                # Plays the fruit_sound effect
                self.fruit_sound.play()
                
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
        
        # Renders the borders
        self.grid.draw_borders(self.screen, self.border_color)
        
        # Renders the grid if debugging is True, renders the background otherwise
        self.grid.draw_grid(self.screen, SnakeGame.DEBUG)
        
        # Renders the score text
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (0, 0))
        
        # Renders the snake
        self.snake.draw_snake(self.screen)
        
        # Renders the fruit
        self.fruit.draw_fruit(self.screen)
        
        pygame.display.flip()

S = SnakeGame()
S.run()