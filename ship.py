import pygame
class Ship():
    """ 飞船初始化 """
    def __init__(self,screen,ship_settings,name):
        #加载图片以及设定位置
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load('resource\Plants\Peashooter.png')
        self.rect = self.image.get_rect()
        
        self.name = name

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.rect.bottom = self.screen_rect.bottom

        #移动
        self.speed_factor = ship_settings.speed_factor

        self.ship_mv_rightflag = False
        self.ship_mv_leftflag = False
        self.ship_mv_upflag = False
        self.ship_mv_downflag = False
        

    def blitship(self):
        """ 绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update_ship(self,ai_settings,ship_settings):
        """ 更新飞船位置"""
        if self.ship_mv_rightflag :
            if self.rect.centerx <= ai_settings.width:
                self.rect.centerx += ship_settings.speed_factor
        if self.ship_mv_leftflag :
            if self.rect.centerx >= ship_settings.speed_factor+1:
                self.rect.centerx -= ship_settings.speed_factor
        if self.ship_mv_downflag :             
            if self.rect.centery < ai_settings.height:                 
                self.rect.centery += ship_settings.speed_factor
        if self.ship_mv_upflag:
            if self.rect.centery > ship_settings.speed_factor+100:
                self.rect.centery -= ship_settings.speed_factor
    def center_ship(self):
        """让飞船在屏幕下居中"""
        self.rect.centerx = self.screen_rect.centerx   
        self.rect.bottom = self.screen_rect.bottom
    def load_image(self,name):
        """ 加载不同的飞船"""
        self.name = name
        if self.name == "Peashooter" :
            #加载飞船图像，并设置速度
            self.image = pygame.image.load('resource\Plants\Peashooter.png')
            self.speed_factor += 1 
            
        elif self.name == "SnowPea" :
            #加载子弹图像，并设置速度
            self.image = pygame.image.load('resource\Plants\SnowPea.png')
            self.speed_factor += 3
           
        elif self.name == "Threepeater" :
            #加载子弹图像，并设置速度
            self.image = pygame.image.load('resource\Plants\Peashooter.png')
            self.speed_factor += 5
            
        elif self.name == "Ironman" :
            #加载子弹图像，并设置速度
            self.image = pygame.image.load('resource\Plants\Ironman.png')
            self.speed_factor += 10

