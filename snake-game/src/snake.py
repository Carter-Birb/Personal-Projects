import pygame

class Snake:
    
    def __init__(self, starting_pos:tuple, starting_dir:str, color, size:int):
        self.body = [starting_pos]
        self.direction = starting_dir
        self.color = color
        self.size = size
    
    def move(self):
        '''
        moves the snake depending on the direction
        '''
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        self.body = [new_head] + self.body[:-1]
    
    def grow(self):
        '''
        grows the snake by a length of 1 when the snake collides with a fruit
        '''
        tail_x, tail_y = self.body[-1]
        if self.direction == "UP":
            new_segment = (tail_x, tail_y + 1)
        elif self.direction == "DOWN":
            new_segment = (tail_x, tail_y - 1)
        elif self.direction == "RIGHT":
            new_segment = (tail_x - 1, tail_y)
        elif self.direction == "LEFT":
            new_segment = (tail_x + 1, tail_y)
        self.body.append(new_segment)
    
    def change_direction(self, new_direction):
        '''
        change sthe snake's movement direction
        '''
        self.direction = new_direction
    
    def check_collision(self, debugging) -> bool:
        '''
        checks if the head of the snake has collided with another segment of the snake
        '''
        head = self.body[0]
        if debugging and head in self.body[1:]:
            print("Snake touched")
        return head in self.body[1:]
                    
    
    def draw_snake(self, screen):
        '''
        draws the snake depending on its length
        '''
        for segment in self.body:
            grid_x, grid_y = segment
            pygame.draw.rect(screen, self.color, pygame.Rect(grid_x * self.size, grid_y * self.size, self.size, self.size))