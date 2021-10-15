import pygame
import random
import math


# Random
#   valueND = random.randint(0,3)
#     if valueND==1:
#         eIMG = pygame.image.load('2.png')
#         enemyImg.append(eIMG)
#         enemyX.append(random.randint(0, 800))
#         enemyY.append(random.randint(50, 150))
#         enemyX_change.append(0.3)
#         enemyY_change.append(40)
#     else:
#         eIMG = pygame.image.load('5.png')
#         enemyImg.append(eIMG)
#         enemyX.append(random.randint(0, 800))
#         enemyY.append(random.randint(50, 150))
#         enemyX_change.append(0.3)
#         enemyY_change.append(40)


# Initilization
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Background of the game
bg = pygame.image.load("a.jpg")


# Title and icon of the game
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("3.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("1.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    valueND = random.randint(0, 3)
    if valueND == 1:
        eIMG = pygame.image.load("2.png")
        enemyImg.append(eIMG)
        enemyX.append(random.randint(0, 800))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(0.3)
        enemyY_change.append(40)
    else:
        eIMG = pygame.image.load("5.png")
        enemyImg.append(eIMG)
        enemyX.append(random.randint(0, 800))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(0.3)
        enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load("4.png")
bulletX = 0
bulletY = 480
bullet_state = "ready"
bulletX_change = 0
bulletY_change = 0.7

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

# Game over
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Winner
win_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    scores = font.render("Score :" + str(score), True, (255, 255, 255))
    screen.blit(scores, (x, y))


def game_over_text():
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))


def winner():
    win = win_font.render("Winner", True, (255, 255, 255))
    screen.blit(win, (240, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Bullet Shot
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Collision Check
def isColliscon(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Main Program
running = True
while running:
    # screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                print("Keystroke has been released")

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 740:
        playerX = 740

    for i in range(num_of_enemies):
        # game over
        if enemyY[i] > 640:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 740:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -0.3

        if score == 100:
            winner()
            break
        collision = isColliscon(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(0, 50)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
