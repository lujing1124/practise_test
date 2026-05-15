import pygame
from pygame.locals import *
import time
import sys


# 初始化pygame
pygame.init()
screen_width=640
scree_height=480
screen = pygame.display.set_mode(size=(screen_width,scree_height))
BLOCK_SIZE = 20
direction_dict = {
    pygame.K_UP:(0, -BLOCK_SIZE),
    pygame.K_RIGHT:( BLOCK_SIZE, 0),
    pygame.K_DOWN:( 0, BLOCK_SIZE),
    pygame.K_LEFT:(-BLOCK_SIZE, 0)
}
head_dict = {
    pygame.K_UP:180,
    pygame.K_RIGHT:90,
    pygame.K_DOWN:0,
    pygame.K_LEFT:270
}
COLOR = (100,100,100)

class Snake:
    def __init__(self):
        self.score = 0
        self.direction = pygame.K_RIGHT  #上0右1下2左3
        self.snake_body = [            
            pygame.Rect(10*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(9*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(8*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(7*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(6*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(5*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(4*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(3*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(2*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(1*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(0*BLOCK_SIZE,2*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
        ]
        self.snake_head_image = pygame.transform.scale(pygame.image.load("res/head-red.png"),(BLOCK_SIZE,BLOCK_SIZE))

    def draw(self, screen):       
        for node in self.snake_body[1:]:
            pygame.draw.rect(screen,(0,0,255),node,border_radius=3) 

        head:pygame.Rect = self.snake_body[0]
        head_image = pygame.transform.rotate(self.snake_head_image,head_dict[self.direction])
        screen.blit(head_image,(head.x, head.y))

    def update_direction(self, new_dir):
        LR = (pygame.K_LEFT, pygame.K_RIGHT)
        UD = (pygame.K_UP, pygame.K_DOWN)
        if self.direction in LR and new_dir in LR:
            return
        if self.direction in UD and new_dir in UD:
            return
        self.direction = new_dir

    # def is_direction_enable(self,event_key):
    #     self.direction = event_key

    def move(self):       
        
        # if self.direction == 0:
        #     new_node.x += 0
        #     new_node.y -= BLOCK_SIZE

        new_node = self.snake_body[0].copy()
        new_node.x += direction_dict[self.direction][0]
        new_node.y += direction_dict[self.direction][1]
        
        self.snake_body.insert(0, new_node)
        self.snake_body.pop()

    def grow(self):
        self.score += 1
        new_node = self.snake_body[-1].copy()
        self.snake_body.append(new_node)
    
import random


class Food:
    def __init__(self, node):
        self.node = node #pygame.Rect(x*BLOCK_SIZE,y*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
        # (self.x,self.y) = get_food_position()
    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),self.node,border_radius=3)
     
    @staticmethod   
    def get_food_position(snake:Snake):
    # (24,32)
        while True:
            x = random.randint(0,31)
            y = random.randint(0,23)
            new_food_node = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
            if new_food_node not in snake.snake_body:
                return new_food_node

class Game:
    def __init__(self):
        icon_image = pygame.image.load("res/icon.png")
        pygame.display.set_icon(icon_image)
        pygame.display.set_caption("贪吃蛇")

        self.bg_image = pygame.image.load("res/bg.png")
        self.bg_image = pygame.transform.scale(self.bg_image,(screen_width,scree_height))

    def start(self):
        clock = pygame.time.Clock()
        snake = Snake()
        food = Food(Food.get_food_position(snake))    
        game_over = False

        while True:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    print('close')
                    pygame.display.quit()
                    exit(0)
                elif event.type == pygame.KEYDOWN:
                    print('keybord an', event.key)
                    # 上、下、左、右、空格
                    if game_over:
                        if event.key == pygame.K_q:
                            pygame.display.quit()
                            exit(0)
                        else:
                            snake = Snake()
                            food = Food(Food.get_food_position(snake))    
                            game_over = False
                    elif event.key == pygame.K_UP:
                        print('keyUp')
                        snake.update_direction(pygame.K_UP)
                    elif event.key == pygame.K_RIGHT:
                        print('keyR')
                        snake.update_direction(pygame.K_RIGHT)
                    elif event.key == pygame.K_DOWN:
                        print('keyD')
                        snake.update_direction(pygame.K_DOWN)
                    elif event.key == pygame.K_LEFT:
                        print('keyL')
                        snake.update_direction(pygame.K_LEFT)
            if not game_over:
                snake.move()
                if snake.snake_body[0] == food.node:
                    # x, y = get_food_position(snake)
                    food = Food(Food.get_food_position(snake))   #刷新食物
                    snake.grow()
                    
                # 碰到墙壁
                snake_head = snake.snake_body[0]
                if snake_head.x <0 or snake_head.x >= 640 \
                or snake_head.y <0 or snake_head.y >= 480:
                    print('111')
                    game_over = True
                
                # 碰到自己
                if snake_head in snake.snake_body[1:]:
                    print('222')
                    game_over = True

            screen.blit(self.bg_image,(0,0))#放置背景图

            # 绘制网格
            for y in range(0,scree_height,BLOCK_SIZE):
                start =(0,y)
                end = (screen_width,y)
                pygame.draw.line(screen,COLOR,start,end,1)

            for y in range(0,screen_width,BLOCK_SIZE):
                start = (y,0)
                end = (y,scree_height)
                pygame.draw.line(screen,COLOR,start,end,1)
            
            # screen.blit(plane_image,(160,30))

            # 放置蛇
            
            snake.draw(screen)
        
            # 食物
            food.draw(screen)
            
            #游戏结束，渲染文字
            if game_over:
                font = pygame.font.SysFont('SimHei',30)
                text = font.render("Game over!",True,(0,0,0))   
                text2 = font.render("score: {}".format(snake.score),True,(0,0,0))   
                text3 = font.render("press any key restart!",True,(0,0,0))   
                    
                screen.blit(text,(160,120))    
                screen.blit(text2,(160,180))    
                screen.blit(text3,(160,220))    
            
            pygame.display.flip()
            clock.tick(5) #fps 5

game = Game()
game.start()


      




