import pygame
from random import randint

class Fruit:
    
    def __init__(self, grid_rows, grid_columns, snake_body, color ,size):
        self.position = self.generate_fruit_location(grid_rows, grid_columns, snake_body)
        self.color = color
        self.size = size
    
    def generate_fruit_location(self, grid_rows, grid_columns, snake_body) -> tuple:
        while True:
            fruit_x, fruit_y = randint(1, grid_columns - 2), randint(1, grid_rows - 2)
            # Check if the fruit position is colliding with the snake body
            if (fruit_x, fruit_y) not in snake_body:
                return fruit_x, fruit_y  # Return the valid position
        
    
    def draw_fruit(self, screen):
        grid_x, grid_y = self.position
        pygame.draw.rect(screen, self.color, pygame.Rect(grid_x * self.size, grid_y * self.size, self.size, self.size))