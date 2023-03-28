import pygame, sys
from pygame.locals import *
from paddle import *
from settings import *


pygame.init()

#window
win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("PONG")
fps_clock = pygame.time.Clock()

#font for texts
font = pygame.font.Font('freesansbold.ttf', 32)

#game loop
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()   
        
    '''game logic'''
    
    ball.check_bounce(p1, p2, win_w)
    if ball.pos_x >= win_w:
        split_score[0] = (f"{score1}")
        score1 += 1
        Score = "".join(split_score)
        ball = Ball(b_x, b_y, b_r, redirect_x,redirect_y, b_speed)
    elif ball.pos_x <= 0:
        split_score[2] = (f"{score2}")
        score2 += 1
        Score = "".join(split_score)        
        ball = Ball(b_x, b_y, b_r, redirect_x,redirect_y, b_speed)
    p1.movement(win_h, True)
    p2.movement(win_h, False)
    ball.movement(win_h)

    #menu screen
    if menu_screen:
        win.fill("crimson")

        play_text = font.render("Press SPACE to play the game or ESC to quit", True, "white")
        play_rect = play_text.get_rect()
        play_rect.center = (win_w/2, win_h/2)
        win.blit(play_text, play_rect)

        if keys[pygame.K_SPACE]:
            menu_screen = False
            main_screen = True
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    #game/main
    elif main_screen:    
        #draw
        win.fill("white")

        pygame.draw.line(win, "grey", (win_w/2, 0), (win_w/2, win_h), 1)

        ball.draw(win, "black")
        p1.draw("blue", win)
        p2.draw("red", win)

        score_text = font.render(Score, True, "black") 
        score_rect = score_text.get_rect()
        score_rect.center = (win_w/2, 20)
        win.blit(score_text, score_rect)

        if split_score[0] == str(score_goal) or split_score[2] == str(score_goal):
            main_screen = False
            end_screen = True
    
    #gaame over screen
    elif end_screen:
        win.fill("black")

        reset_text = font.render("Press SPACE to reset the game or ESC to quit", True, "white")
        reset_rect = reset_text.get_rect()
        reset_rect.center = (win_w/2, win_h/2)
        win.blit(reset_text, reset_rect)

        if keys[pygame.K_SPACE]:
            Score = "0:0"
            end_screen = False
            main_screen = True

        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    fps_clock.tick(FPS)