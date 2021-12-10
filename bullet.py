import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ 子弹初始化 """
    def __init__(self,bullet_settings,screen,ship):
        """初始化子弹"""

        super(Bullet,self).__init__()

        self.screen = screen

        self.bullet_settings = bullet_settings
        self.speed_factor = bullet_settings.speed_factor

        
        self.image = pygame.image.load('resource\Bullets\PeaNormal.png')
        self.rect = self.image.get_rect()

        # 从飞船中间发射子弹
        self.rect.x = ship.rect.centerx
        self.rect.y = ship.rect.top

        #储存用小数表示的位置
        self.y = float(ship.rect.y)

        self.load_image(ship)



    def load_image(self,ship):
        """ 加载不同的子弹"""
        if ship.name == "Peashooter" :
            #加载子弹图像，并设置速度
            self.image = pygame.image.load('resource\Bullets\PeaNormal.png')
            self.speed_factor += 2 
            
        elif ship.name == "SnowPea" :
            #加载子弹图像，并设置速度
            self.image = pygame.image.load('resource\Bullets\PeaIce.png')
            self.speed_factor += 3
           
        elif ship.name == "Threepeater" :
            #加载子弹图像，并设置速度
            self.image = pygame.image.load('resource\Bullets\PeaNormalExplode.png')
            self.speed_factor += 5

        elif ship.name == "Ironman" :
            self.image = pygame.image.load('resource\Bullets\PalmCannon.png')
            self.speed_factor += 10
            


        

        

    def update(self):
        """ 在屏幕绘制绝招"""
        
        """向上移动"""
        self.y -= self.speed_factor
        self.rect.y = self.y


        
        
        



        


