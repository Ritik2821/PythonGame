import pygame
import random
import math

from pygame import mixer

# initialize pygame
pygame.init()

# creating screeen
screen = pygame.display.set_mode((800, 600))  # width, height

# Background
background = pygame.image.load('spacebackground.png')

#BACKGROUND SOUND
mixer.music.load('background.wav')
mixer.music.play(-1)   # sound will play infinitly on the screen by adding -1 in parenthesis

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('startup.png')
pygame.display.set_icon(icon)

# PLAYER
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# ENEMY
enemyImg=  []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies= 1

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX .append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# enemyImg = pygame.image.load('enemy.png')
# enemyX = random.randint(0, 735)
# enemyY = random.randint(50, 150)
# enemyX_change = 2
# enemyY_change = 40

# BULLET

# READY STATE-YOU CANT SEE THE BULLET ON THE SCREEN
# FIRE -THE BULLET IS CURRENTLY MOVING
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"

#SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

#GAME OVER TEXT
game_over_font = pygame.font.Font('freesansbold.ttf', 70)


def show_score(x, y):
    score= font.render("Score :" +str(score_value) , True ,(255, 255, 255))
    screen.blit(score, (x , y))

def game_over_text():
    over_text = game_over_font.render("GAME OVER" , True, (255, 0, 0))
    screen.blit(over_text, (200, 250))



def player(x, y):
    # blit=draw the image on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    # blit=draw the image on the screen
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance <27:
        return True
    else:
        return False


# game loop
running = True
while running:
    # RGB-RED GREEN BLUE
    screen.fill((0, 0, 0))
    # BACKGROUND
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN:

            # print(" A keystroke is pressed ")
            if event.key == pygame.K_LEFT:
                playerX_change = - 3
                # print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
                # print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound=mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    # GET THE CURRENT X COORDINATE OF SPACESHIP
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # coordinates stop changing
                # print("Keystroke has been released")

    playerX += playerX_change
    # 736 pixel beacuse image size is 64 px thats  why to take whole image into consideration
    # (800-64)pixel.
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

#ENEMY MOVEMENT
    for i in range(num_of_enemies):

        #GAME OVER
        if enemyY[i]> 430:
            for j in  range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        # 736 pixel beacuse image size is 64 px thats  why to take whole image into consideration
        # (800-64)pixel.
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] = enemyY[i] + enemyY_change[i]

        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] = enemyY[i] + enemyY_change[i]

        # COLLISION
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480  # RESET BULLET TO STARTING POINT
            bullet_state = "ready"  # IF BULLET CANT BE SEEN THEN ITS IN READY STATE
            score_value += 1
            #print(score)
            enemyX[i] = random.randint(0, 735)  # WE USED THESE STATEMENT TO POSITION THE ENEMY BACK TO ITS IN
            enemyY[i] = random.randint(50, 150)  # INITIAL POSITION AFTER THE BULLET HITS IT

        enemy(enemyX[i], enemyY[i], i)

    # BULLET MOVEMENT
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #COLLISION
    # collision=isCollision(enemyX,enemyY,bulletX,bulletY)
    # if collision:
    #     bulletY=480   #RESET BULLET TO STARTING POINT
    #     bullet_state="ready" # IF BULLET CANT BE SEEN THEN ITS IN READY STATE
    #     score+=1
    #     print(score)
    #     enemyX = random.randint(0, 735)    #WE USED THESE STATEMENT TO POSITION THE ENEMY BACK TO ITS IN
    #     enemyY = random.randint(50, 150)    # INITIAL POSITION AFTER THE BULLET HITS IT

    player(playerX, playerY)
    show_score(textX , textY)
    # enemy(enemyX, enemyY)
    pygame.display.update()
