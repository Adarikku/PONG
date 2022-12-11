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

    #score logic
#    if b_x == 0 + b_r:
#        split_score[0] = (f"{score1}")
#        score1 += 1
#        Score = "".join(split_score)
#        b_x, b_y = win_w/2, win_h/2
#    elif b_x == win_w - b_r:
#        split_score[2] = (f"{score2}")
#        score2 += 1
#        Score = "".join(split_score)
#        b_x, b_y = win_w/2, win_h/2

    ball.movement(p1, win_h, win_w)
    ball.movement(p2, win_h, win_w)
    p1.movement(win_h, True)
    ball.check_bounce(p1, win_h, win_w)
    p2.movement(win_h, False)
    ball.check_bounce(p2, win_h, win_w)
    #scores.counting(ball, win_h, win_w) #z nějakého důvodu stuckne ball uprostřed

    #main screen
    if main_screen:
        win.fill("crimson")

        play_text = font.render("Press SPACE to play the game or ESC to quit", True, "white")
        play_rect = play_text.get_rect()
        play_rect.center = (win_w/2, win_h/2)
        win.blit(play_text, play_rect)

        if keys[pygame.K_SPACE]:
            main_screen = False
            game_is_running = True
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    #game/main
    elif game_is_running:    
        #draw
        win.fill("white")
        ball.draw(win, "black")
        p1.draw("blue", win)
        p2.draw("red", win)
        pygame.draw.line(win, "grey", (win_w/2, 0), (win_w/2, win_h), 1)
        score_text = font.render(Score, True, "black") 
        score_rect = score_text.get_rect()
        score_rect.center = (win_w/2, 20)
        win.blit(score_text, score_rect)
        if split_score[0] == "5" or split_score[2] == "5":
            game_is_running = False
            end_screen = True
    
    #gaame over screen
    elif end_screen:
        win.fill("black")
        reset_text = font.render("Press SPACE to reset the game or ESC to quit", True, "white")
        reset_rect = reset_text.get_rect()
        reset_rect.center = (win_w/2, win_h/2)
        win.blit(reset_text, reset_rect)

        if keys[pygame.K_SPACE]:
            Score = "0 : 0"
            end_screen = False
            game_is_running = True

        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    fps_clock.tick(FPS)