
import sys

import pygame

#编组
from pygame.sprite import Group

#设置参数
from settings import Display_settings,Ship_settings,Bullet_settings,Trick_settings,Alien_settings,Sun_settings

#引入游戏元素
from bullet import Bullet
from ship import Ship
from alien import Alien
from trick import Trick
from gamestats import GameStats
from botton import Botton
from scoreboard import Scoreboard

from sun import Sun
from chooser import Chooser
#功能函数
import functions 

def run_game():
    pygame.init()

    #屏幕标题设置
    pygame.display.set_caption("植物大战僵尸雷霆战机版v0.1")

    #设置参数：
    #屏幕
    ai_settings = Display_settings()
    #飞船
    ship_settings = Ship_settings()
    #子弹
    bullet_settings = Bullet_settings()
    #大招
    trick_settings = Trick_settings()
    #外星人
    alien_settings = Alien_settings()
    #阳光
    sun_settings = Sun_settings()

    #屏幕宽高设置函数
    screen = pygame.display.set_mode(
        (ai_settings.width,ai_settings.height))
    
    #创建一个用于存储游戏信息的实例
    stats = GameStats(ship_settings)
    

    #创建一个计分板
    scoreboard =Scoreboard(ai_settings,screen,stats)
    
    #飞船定义
    ship = Ship(screen,ship_settings,"Peashooter")

    #阳光定义   
    #阳光编组,创建阳光
    suns = Group()

    #选择面板定义
    chooser = Chooser(screen)

    
    #子弹编组，创建子弹
    bullets = Group()
    
    functions.creat_bullets(bullet_settings,bullets,screen,ship)
    
    #绝招定义
    #trick = Trick(screen)
    tricks = Group()

    #外星人定义
    #外星人编组,创建多行行外星人
    aliens = Group()

    functions.create_fleet(ai_settings,alien_settings,screen,ship,aliens,stats)

    #创建Play按钮
    play_botton = Botton(ai_settings,screen,"PLAY")
    
    

    while True:
        #检测鼠标及键盘事件
        functions.check_events(ai_settings,screen,stats,play_botton,ship,tricks,suns,chooser)
        
        #开始按钮的创建
        functions.play_botton(ai_settings,screen,stats,play_botton)
        
        ##游戏开始：
        if stats.game_active :
            ##屏幕刷新
            functions.update_screen(
                
            ai_settings,

            screen,

            ship,ship_settings,

            bullets,bullet_settings,

            tricks,

            alien_settings,aliens,

            scoreboard,

            suns,sun_settings,
            
            stats,

            chooser
            )

            

            #检测子弹和大招是否击中外星人，击中则消灭,且增加得分
            functions.collision(aliens,bullets,stats,alien_settings) 
            
                
            #检测外星人是否与飞船相撞，以及外星人是否到达底部
            if functions.game_over(screen,ship,aliens) :
                functions.reborn(ai_settings,alien_settings,stats,screen,ship,aliens,bullets)




            

            
run_game()
