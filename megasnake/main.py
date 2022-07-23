import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 576))
pygame.display.set_caption('MEGA SNEK 9: HOUSE OF PAIN')
# grid is 800/32=24 by 576/32=18
grid=32

headX=10
headY=10
direction=3
def head(x,y):
    pygame.draw.rect(screen,(0,128,0),(x*grid,y*grid,32,32))
def score_text(x,y,score):
    tickrate_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(tickrate_text, (x, y))
def game_over(x,y,score):
    tickrate_text = font.render(f'You lose!   Score: {score}', True, (255, 255, 255))
    screen.blit(tickrate_text, (x, y))
def body(cord_tuple):
    x,y = cord_tuple
    pygame.draw.rect(screen,(0,64,0),(x*grid,y*grid,32,32))

# foodX=random.randint(0,24)
foodX=10
# foodY=random.randint(0,17)
foodY=5
def collision(head_tuple):
    global lost
    x,y = head_tuple
    if head_tuple in pos_memory:
        lost=True
    if x>24:
        lost=True
    if x<0:
        lost=True
    if y>17:
        lost=True
    if y<0:
        lost=True

snake_size=0
def food(x,y):
    pygame.draw.rect(screen,(100,0,0),((x*grid,y*grid),(32,32)))
font = pygame.font.Font('freesansbold.ttf',32)
tickrate=0
pos_memory = []
running = True
food_eaten=False
lost=False
execute=True
while running:
    screen.fill((0, 0, 0))
    # TICKRATE
    if tickrate==5000:
        tickrate=0
    tickrate+=1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and execute:
            if event.key == pygame.K_d and direction != 2:
                direction = 0
                execute=False
            if event.key == pygame.K_s and direction != 3:
                direction=1
                execute = False
            if event.key == pygame.K_a and direction != 0:
                direction=2
                execute = False
            if event.key == pygame.K_w and direction != 1:
                direction=3
                execute = False
    if tickrate==1:
        if not lost:
            score_text(10, 10, snake_size)
            if snake_size==0:
                pos_memory=[(headX,headY)]
            else:
                pos_memory.append((headX, headY))
                while snake_size!=len(pos_memory):
                    pos_memory.pop(0)
                for i in range(snake_size):
                    # print(f'{i}: {pos_memory[i]}')
                    body(pos_memory[i])

            match direction:
                case 0:
                    headX+=1
                case 1:
                    headY += 1
                case 2:
                    headX -= 1
                case 3:
                    headY -= 1
                case 4:
                    pass
            execute=True
            print(pos_memory)
            if food_eaten:
                foodX = random.randint(0, 24)
                foodY = random.randint(0, 17)
                while (foodX,foodY) in pos_memory:
                    foodX=random.randint(0,24)
                    foodY=random.randint(0,17)
                food_eaten=False
            else:
                if headX==foodX and headY==foodY:
                    food_eaten=True
                    snake_size+=1
            collision((headX,headY))

            food(foodX,(foodY))
            head(headX,headY)
        if lost:
            screen.fill((0, 0, 0))
            game_over(200,250,snake_size)

        pygame.display.update()
