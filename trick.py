import pygame
from pygame.sprite import Sprite
class Trick(Sprite):
    """ 对飞船发射大招进行管理的类"""
    def __init__(self,screen):

       """初始化大招"""

       super(Trick,self).__init__()

       self.flag = False

       self.screen = screen
       self.screen_rect = screen.get_rect()
       
       self.image = pygame.image.load('images\Boom.png')
       self.rect = self.image.get_rect()

       self.rect.centerx = self.screen_rect.centerx
       self.rect.centery = self.screen_rect.centery
   
       
       


       





    


