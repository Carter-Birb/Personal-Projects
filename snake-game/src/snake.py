import pygame


class Snake:
    
    def __init__(self, starting_pos:tuple, starting_dir:str, color, size:int):
        self.body = [starting_pos]
        self.direction = starting_dir
        self.color = color
        self.size = size
        self.prev_tail_position = starting_pos  # Save the initial tail position
    
    def move(self):
        '''
        Moves the snake depending on the direction.
        The tail stays the same until `grow()` is called.
        '''
        head_x, head_y = self.body[0]
        
        # Save the current tail position (before moving)
        self.prev_tail_position = self.body[-1]
        
        # Determine the new head position based on the current direction
        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        
        # Move the snake by adding the new head and removing the tail
        self.body = [new_head] + self.body[:-1]
    
    def grow(self):
        '''
        Grows the snake by adding the previous tail position as a new segment.
        '''
        # Append the previous tail position to the snake body
        self.body.append(self.prev_tail_position)
    
    def change_direction(self, new_direction):
        '''
        Changes the snake's movement direction.
        '''
        self.direction = new_direction
    
    def check_collision(self, debugging) -> bool:
        '''
        Checks if the head of the snake has collided with another segment of the snake.
        '''
        head = self.body[0]
        if debugging and head in self.body[1:]:
            print("Snake touched")
        return head in self.body[1:]
    
    def draw_snake(self, screen):
        '''
        Draws the snake depending on its length.
        '''
        for segment in self.body:
            grid_x, grid_y = segment
            pygame.draw.rect(screen, self.color, pygame.Rect(grid_x * self.size, grid_y * self.size, self.size, self.size))