import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ 表示单个外星人的类"""
    def __init__(self,alien_settings,screen,name):
        """ 初始化外星人"""
        
        super(Alien,self).__init__()
        
        self.screen = screen 
        
        self.name = name
        self.alien_settings = alien_settings
        self.speed_factor = alien_settings.x_speed

        #加载外星人图像，并设置rect属性
        self.image = pygame.image.load('resource\Zombies\Zombie.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height+50

        #存储每个外星人的准确位置
        self.x = float(self.rect.x)

        self.load_image(name)
       

        

    def load_image(self,name):
        """ 加载不同的僵尸"""
        self.name = name
        if self.name == "Zombie" :
            self.image = pygame.image.load('resource\Zombies\Zombie.png')
        
        elif self.name == "BucketheadZombie"  :
            #加载僵尸图像，并设置速度
            self.image = pygame.image.load('resource\Zombies\FlagZombie.png')
            self.speed_factor += 1 
            
        elif self.name == "ConeheadZombie" :
            #加载僵尸图像，并设置速度
            self.image = pygame.image.load('resource\Zombies\ConeheadZombie.png')
            self.speed_factor += 2
           
        elif self.name == "FlagZombie" :
            #加载僵尸图像，并设置速度
            self.image = pygame.image.load('resource\Zombies\\NewspaperZombie.png')
            self.speed_factor += 3

        elif self.name == "NewspaperZombie" :
            #加载僵尸图像，并设置速度
            
            self.image = pygame.image.load('resource\Zombies\BucketheadZombie.png')
            self.speed_factor += 4

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True


    def update(self):
        """向右或向左移动外星人"""
        self.x +=  (self.speed_factor*self.alien_settings.fleet_direction)
        self.rect.x = self.x


    





        


