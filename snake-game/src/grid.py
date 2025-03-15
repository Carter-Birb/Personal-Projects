import pygame
from time import time

class Grid:
    
    # Within the grid: 0 = blank space, 1 = snake, 2 = fruit, 3 = borders
    
    def __init__(self, width, height, cell_size):
        self.cell_size = cell_size
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.create_borders()
        
        # Border attributes
        self.border_size = cell_size
        
        # Begin debug timer
        self.snake_debug = time()
        self.interval = 1
        
    
    def update_snake(self, snake_body: list[tuple], debugging):
        '''
        updates the snake's position based on the coordinates provided
        '''
        # Preserve borders and only clear the inner cells (not borders)
        for y in range(self.rows):
            for x in range(self.columns):
                if self.grid[y][x] != 3:  # Keep borders intact
                    self.grid[y][x] = 0  # Clear the inner grid cells

        # Update the grid with the snake's current position
        for segment in snake_body:
            grid_x, grid_y = segment
            self.grid[grid_y][grid_x] = 1  # Set snake body position

        current_debug = time()
        if debugging and current_debug - self.snake_debug >= self.interval:
            print(f"Snake head in position: ({grid_x}, {grid_y})")
            self.snake_debug = current_debug
    
    def place_fruit(self, fruit_position:tuple, debugging):
        '''
        places a fruit within the grid
        '''
        grid_x, grid_y = fruit_position
        self.grid[grid_y][grid_x] = 2
        
        if debugging:
            print(f"Fruit placed at position ({grid_x}, {grid_y})")
    
    def create_borders(self):
        '''
        creates the borders of the game within the grid variable
        '''
        # Mark the borders logically within the grid list
        for x in range(self.columns):
            self.grid[0][x] = 3
            self.grid[self.rows - 1][x] = 3
        for y in range(self.rows):
            self.grid[y][0] = 3
            self.grid[y][self.columns - 1] = 3
    
    def draw_borders(self, screen, border_color):
        # Draw the borders visually
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 3:
                    rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, border_color, rect)
    
    def draw_grid(self, screen, debugging):
        '''
        draws the grid in a different way depending on whether or not debugging is True or False
        '''
        if debugging:
            for row in range(self.rows):
                for col in range(self.columns):
                    pygame.draw.rect(screen, (25, 25, 25), pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 1)  # Grid lines
        if not debugging:
            for row in range(self.rows):
                for col in range(self.columns):
                    if 1 < row < self.rows - 1 and 1 < col < self.columns - 1:
                        pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(col * self.cell_size, row * self.cell_size, 1, 1))  # Dotted background
    
    def check_border_collision(self, snake_head:tuple, debugging):
        '''
        checks if the snake has collided with a border
        '''
        head_x, head_y = snake_head
        if self.grid[head_y][head_x] == 3:
            if debugging:
                print("Border touched")
            return True
        else:
            return False
    
    def check_fruit_collision(self, head_x, head_y, fruit_x, fruit_y, debugging):
        '''
        checks if the snake has collided with a fruit
        '''
        head = head_x, head_y
        fruit = fruit_x, fruit_y
        if head == fruit:
            if debugging:
                print("Fruit collected")
            return True
        else:
            return False