import pygame
from pygame.locals import *
from paddle import *
from ball import *
from score_board import *

#windoiw
win_w = 1000
win_h = 600
FPS = 100

#some vars
running = True #always
main_screen = True
game_is_running = False
end_screen = False

#paddles
p1_w = 20
p1_h = 120
p1_s = 20
p1_pos = win_h/2

p2_w = 20
p2_h = 120
p2_s = win_w-20-p2_w
p2_pos = win_h/2

speed = 2

#ball
b_x = win_w/2
b_y = win_h/2
b_r = win_h/40
redirect_x = -1
redirect_y = -1
b_speed = 1

#score text
Score = "0 : 0"
split_score = Score.split(" ")
Score = "".join(split_score)
score1, score2 = 1, 1

ball = Ball(b_x, b_y, b_r, -1, -1, b_speed)
p1 = Paddle(p1_w, p1_h, p1_pos, speed, p1_s)
p2 = Paddle(p2_w, p2_h, p2_pos, speed, p2_s)
scores = ScoreBoard(Score, split_score, score1, score2)