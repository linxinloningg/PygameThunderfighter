import pygame
from pygame.sprite import Sprite
import random
class Sun(Sprite):
    """ 阳光创建初始化"""
    def __init__(self,sun_settings,screen):
        
        super(Sun,self).__init__()
        #加载图片以及设定位置
        self.screen =screen
        self.image = pygame.image.load('resource\Background\Sun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        ##阳光设置
        self.sun_settings = sun_settings
        self.speed_factor = sun_settings.x_speed
        

        self.rect.centerx = random.randint(50,self.screen_rect.width)
        self.rect.centery = random.randint(50,self.screen_rect.height)

        

        #存储每个太阳的准确位置
        self.x = float(self.rect.x)

    def blitsun(self):
        """ 绘制阳光"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """向右或向左移动阳光"""
        self.x +=  (self.speed_factor*self.sun_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果阳光位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

