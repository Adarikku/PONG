import pygame

class Ball():

    def __init__(self, pos_x, pos_y, radius, redirect_x, redirect_y, speed):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.redirect_x = redirect_x
        self.redirect_y = redirect_y
        self.speed = speed

    def get_b_x(self):
        return self.pos_x
    
    def get_b_y(self):
        return self.pos_x

    def get_b_r(self):
        return self.pos_x

    def set_b_x(self, x):
        self.pos_x = x

    def set_b_y(self, y):
        self.pos_y = y

    def draw(self, win, color):
        pygame.draw.circle(win, color, (self.pos_x, self.pos_y), self.radius)
    

    def movement(self, pad, win_height, win_width):
        self.pos_x += self.speed * self.redirect_x
        self.pos_y += self.speed * self.redirect_y
        #edges bounce
        if self.pos_y <= 0 + self.radius or self.pos_y >= win_height - self.radius:
            self.redirect_y *= -1
        
    def check_bounce(self, pad, win_height, win_width):    

        #bounce of paddles 
        if self.pos_x == pad.get_sapcer() + self.radius + pad.get_width():
            ### needs tweeks ###
            #if self.pos_y > pad.get_pos() and self.pos_y < pad.get_pos() + pad.get_height()/4 or self.pos_y > pad.get_pos() + 3*pad.get_height()/4 and self.pos_y < pad.get_pos() + pad.get_height():
            #    self.redirect_x *= -1
            #    self.redirect_y = -3
            #elif self.pos_y > pad.get_pos() + pad.get_height()/4 and self.pos_y < pad.get_pos() + pad.get_height()/2 or self.pos_y > pad.get_pos() + pad.get_height()/2 and self.pos_y < pad.get_pos() + 3*pad.get_height()/4:
            #    self.redirect_x *= -1
            #    self.redirect_y = -2
            #else:
            #    self.redirect_x *= -1
            #    self.redirect_y = -1
            if self.pos_y >= pad.get_pos() and self.pos_y <= pad.get_pos() + pad.get_height():
                self.redirect_x *= -1