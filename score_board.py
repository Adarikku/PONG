import pygame

class ScoreBoard():

    def __init__(self, string, split, p1_score, p2_score):
        self.string = string
        self.split = split
        self.p1_score = p1_score
        self.p2_score = p2_score

    def counting(self, ball, win_height, win_width):
        if ball.get_b_x() == 0 + ball.get_b_r():
            self.split[0] = (f"{self.p1_score}")
            self.p1_score += 1
            self.string = "".join(self.split)
            ball.set_b_x(win_width/2)
            ball.set_b_y(win_height/2)
        elif ball.get_b_x() == win_width - ball.get_b_r():
            self.split[2] = (f"{self.p1_score}")
            self.p1_score += 1
            self.string = "".join(self.split)
            ball.set_b_x(win_width/2)
            ball.set_b_y(win_height/2)

    
