import pygame

class Fruit:
    
    def __init__(self, position, color ,size):
        self.position = position
        self.color = color
        self.size = size
    
    def draw_fruit(self, screen):
        grid_x, grid_y = self.position
        pygame.draw.rect(screen, self.color, pygame.Rect(grid_x * self.size, grid_y * self.size, self.size, self.size))