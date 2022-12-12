import pygame

class Paddle():

    def __init__(self, width, height, pos, speed, spacer):
        self.width = width
        self.height = height
        self.pos = pos
        self.speed = speed
        self.spacer = spacer

    def draw(self, color, win):
        pygame.draw.rect(win, color, (self.spacer, self.pos, self.width, self.height))

    def movement(self, win_height, left):
    #paddle movement
        keys = pygame.key.get_pressed()
        if left:
            if keys[pygame.K_w]:
                self.pos -= self.speed
            elif keys[pygame.K_s]:
                self.pos += self.speed
        else:
            if keys[pygame.K_UP]:
                self.pos -= self.speed
            elif keys[pygame.K_DOWN]:
                self.pos += self.speed

    #edges logic
        if left:
            if self.pos == 0:
                self.speed = 0
                if keys[pygame.K_s]:
                    self.speed = 2
            elif self.pos == win_height - self.height:
                self.speed = 0
                if keys[pygame.K_w]:
                    self.speed = 2
        else:
            if self.pos == 0:
                self.speed = 0
                if keys[pygame.K_DOWN]:
                    self.speed = 2
            elif self.pos == win_height - self.height:
                self.speed = 0
                if keys[pygame.K_UP]:
                    self.speed = 2


    def get_pos(self):
        return self.pos
    
    def get_spacer(self):
        return self.spacer
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
        
    