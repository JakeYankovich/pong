import pygame
import random
pygame.init()


gWidth = 650
gHeight = 450

win = pygame.display.set_mode((gWidth, gHeight))

pygame.display.set_caption("Pong") 
myfont = pygame.font.SysFont('candara', 45) 


gameSpeed = 20 #lower is faster

run = True
ball = [300, 300, 25, 25]
ballxvel = -4
ballyvel = -2
playerbar = [10, 0, 25, 100]
loserbar = [615, 200, 25, 100]
white = (255, 255, 255)
ballcolor = (255, 255, 255)
ceiling = pygame.Rect(0, -10, 650, 10)
floor = pygame.Rect(0, 450, 650, 10)
youlose = pygame.Rect(0, 0, 5, 450)
youwin = pygame.Rect(645, 0, 5, 450)
lose = False
won = False
startingtext = ""
bgcolor= (100, 100, 100)
score = [0, 0]
def newballcolor():
    R = random.randint(100,255)
    G = random.randint(100,255)
    B = random.randint(100,255)
    ballcolor = ( R, G, B )
    bgcolor = ( (255-R), (255-G), (255-B) )
    #print("ball color moment", ballcolor)
    return(ballcolor, bgcolor)
while run:
    pygame.time.delay(gameSpeed) #delay between frames
    
    win.fill((bgcolor)) #fill background color
    
    for event in pygame.event.get(): # without this for loop, pygame will go not responding
        if event.type == pygame.QUIT:
            run = False
        
        
        
    #       draw player's bar
    mouspot = pygame.mouse.get_pos()
    playerbar[1] = mouspot[1] -50
    pygame.draw.rect(win, ballcolor, playerbar) 
    
    #for event in pygame.event.get():
    if event.type == pygame.MOUSEMOTION:
        dx, dy = event.rel
    
    
    if ballyvel > 8: 
        loserbar[1] += ballyvel/4
    elif ballyvel > 6:
        loserbar[1] += ballyvel/3
    elif ballyvel > 4:
        loserbar[1] += ballyvel/2
    else: loserbar[1] += ballyvel*2/3
    #if loserbar[1] > ball[1]:
    loserbar[1] -= (  loserbar[1] - (ball[1]  )  )/14
    '''else:
        loserbar[1] -= (loserbar[1] - ball[1])/15 + 1'''
        
    
    #if ball[1] > 225: loserbar[1] +=
    #else: loserbar[1] -= 5
    if loserbar[1] > 375:       # Move AI bar, keep it on screen
        loserbar[1] =  375
    elif loserbar[1] < 0:
        loserbar[1] = 0
    
    
    #draw AI's bar
    pygame.draw.rect(win, ballcolor, loserbar)  
    
    #draw ball
    pygame.draw.rect(win, ballcolor, ball)
    
    #update ball position
    ball[0] += ballxvel
    ball[1] += ballyvel
    
    
    rectbar = pygame.Rect(playerbar[0]+15, playerbar[1], playerbar[2]-15, playerbar[3])
    collide=False                           #check if player hits ball
    if rectbar.collidepoint(ball[0], ball[1]) or rectbar.collidepoint(ball[0], ball[1]+25):
        collide = True
        ballcolor, bgcolor = newballcolor()
    if collide:
        ballxvel = abs(ballxvel)
        ballyvel = ballyvel + dy
        if ballyvel > 12: ballyvel = 12
        elif ballyvel < -12: ballyvel = -12
        #print(ballyvel)
    
    rectloser = pygame.Rect(loserbar)           #check if AI hits ball
    losercollide=False
    if rectloser.collidepoint(ball[0]+25, ball[1]) or rectloser.collidepoint(ball[0]+25, ball[1]+25):
        losercollide = True
        ballcolor, bgcolor = newballcolor()
    if losercollide:
        ballxvel = -abs(ballxvel)
    
    
    if ceiling.collidepoint(ball[0], ball[1]):  #check ceiling collision
        ballcolor, bgcolor = newballcolor()
        ballyvel = abs(ballyvel)
    if floor.collidepoint(ball[0], ball[1]+25): #check floor collision
        ballcolor, bgcolor = newballcolor()
        ballyvel = -abs(ballyvel)
        
    
    if youlose.collidepoint(ball[0], ball[1]): #check if ball goes off left side
        lose = True
        #startingtext = "YOU LOSE"
        ball = [300, 300, 25, 25]
        ballxvel = -4
        ballyvel = -2
        score[1] += 1
    if youwin.collidepoint(ball[0]+25, ball[1]): #check if ball goes off left side
        won = True
        #startingtext = "YOU WIN"
        ball = [300, 300, 25, 25]
        ballxvel = -4
        ballyvel = -2
        score[0] += 1
    if lose or won:            #tells you that you won/lost
        textsurface = myfont.render(startingtext, False, white)
        win.blit(textsurface,(100,60))
    scoretext = "score " + str( score[0] ) + " | " + str( score[1]  )
    #print(scoretext)
    scoresurface = myfont.render( scoretext, False, white)
    win.blit(scoresurface, (200, 80))
    
    collide = losercollide = False
    pygame.display.update() #draw the screen with whatever changes you've made above

pygame.quit()